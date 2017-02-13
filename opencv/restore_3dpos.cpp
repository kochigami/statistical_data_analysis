#include <iostream>
#include <vector>
#include <fstream>
#include <opencv2/core/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/objdetect/objdetect.hpp>
#include <opencv2/features2d/features2d.hpp>
#include <opencv2/calib3d/calib3d.hpp>

int main(int argc, char** argv)
{
  // astra camera calibration parameters
  
  // camera matrix
  // 554.925965 0.000000 322.448605
  // 0.000000 560.790573 264.018102
  // 0.000000 0.000000 1.000000
  
  // distortion
  // 0.081784 -0.713658 0.028528 0.002789 0.000000
    
  // rectification
  // 1.000000 0.000000 0.000000
  // 0.000000 1.000000 0.000000
  // 0.000000 0.000000 1.000000
  
  // projection
  // -3289.852539 0.000000 486.885877 0.000000
  // 0.000000 -628.223572 430.646825 0.000000
  // 0.000000 0.000000 1.000000 0.000000
  

  //カメラパラメータの読み込みとレンズ歪の除去
  cv::Mat img1; //入力画像1
  cv::Mat img2; //入力画像2
  cv::Mat cameraMatrix;
  cv::Mat distCoeffs;
  
  cameraMatrix = cv::Mat_<double>(3,3) << 554.925965, 0.000000, 322.448605, 0.000000, 560.790573, 264.018102, 0.000000, 0.000000, 1.000000;
  distCoeffs = cv::Mat_<double>(5,1) << 0.081784, -0.713658, 0.028528, 0.002789, 0.000000;
  
  //cv::FileStorage fs("camera.xml", CV_STORAGE_READ);
  //fs["intrinsicMat"] >> cameraMatrix;
  //fs["distCoeffs"] >> distCoeffs;
  
  cv::undistort(cv::imread("image1.png"), img1, cameraMatrix, distCoeffs);
  cv::undistort(cv::imread("image2.png"), img2, cameraMatrix, distCoeffs);

  //特徴抽出
  cv::OrbFeatureDetector detector(300);
  cv::OrbDescriptorExtractor descriptorExtractor;

  //cv::Ptr<cv::FeatureDetector> detector = cv::FeatureDetector::create( "SURF" ); //検出器
  //cv::Ptr<cv::DescriptorExtractor> descriptorExtractor = cv::DescriptorExtractor::create( "SURF" ); //特徴量
  cv::Ptr<cv::DescriptorMatcher> matcher = cv::DescriptorMatcher::create("BruteForce"); //対応点探索方法の設定

  std::vector<cv::KeyPoint> keypoints1, keypoints2;
  cv::Mat descriptor1, descriptor2;
  detector.detect(img1, keypoints1);
  descriptorExtractor.compute(img1, keypoints1, descriptor1);

  detector.detect(img2, keypoints2);
  descriptorExtractor.compute(img2, keypoints2, descriptor2);

  //対応点の探索
  std::vector<cv::DMatch> dmatch;
  std::vector<cv::DMatch> dmatch12, dmatch21;

  matcher->match(descriptor1, descriptor2, dmatch12); //img1 -> img2
  matcher->match(descriptor2, descriptor1, dmatch21); //img2 -> img1

  for (size_t i = 0; i < dmatch12.size(); ++i)
    {
      //img1 -> img2 と img2 -> img1の結果が一致しているか検証
      cv::DMatch m12 = dmatch12[i];
      cv::DMatch m21 = dmatch21[m12.trainIdx];

      if (m21.trainIdx == m12.queryIdx)
	dmatch.push_back( m12 );
    }

  //十分な数の対応点があれば基礎行列を推定
  if (dmatch.size() > 5)
    {
      std::vector<cv::Point2d> p1;
      std::vector<cv::Point2d> p2;
      //対応付いた特徴点の取り出しと焦点距離1.0のときの座標に変換
      for (size_t i = 0; i < dmatch.size(); ++i)
	{
	  cv::Mat ip(3, 1, CV_64FC1);
	  cv::Point2d p;

	  ip.at<double>(0) = keypoints1[dmatch[i].queryIdx].pt.x;
	  ip.at<double>(1) = keypoints1[dmatch[i].queryIdx].pt.y;
	  ip.at<double>(2) = 1.0;
	  ip = cameraMatrix.inv()*ip;
	  p.x = ip.at<double>(0);
	  p.y = ip.at<double>(1);
	  p1.push_back( p );

	  ip.at<double>(0) = keypoints2[dmatch[i].trainIdx].pt.x;
	  ip.at<double>(1) = keypoints2[dmatch[i].trainIdx].pt.y;
	  ip.at<double>(2) = 1.0;
	  ip = cameraMatrix.inv()*ip;
	  p.x = ip.at<double>(0);
	  p.y = ip.at<double>(1);
	  p2.push_back( p );
	}

      cv::Mat mask; //RANSACの結果を保持するためのマスク
      cv::Mat essentialMat = cv::findEssentialMat(p1, p2, 1.0, cv::Point2f(0, 0), cv::RANSAC, 0.9999, 0.003, mask);
      //cv::Mat essentialMat = cv::findEssentialMat(p1, p2);
      std::cout << "Essential Matrix\n" << essentialMat << std::endl;
      
      cv::Mat r, t;
      cv::recoverPose(essentialMat, p1, p2, r, t);
      std::cout << "R:\n" << r << std::endl;
      std::cout << "t:\n" << t << std::endl;
    
      cv::Mat prjMat1, prjMat2;
      prjMat1 = cv::Mat::eye(3, 4, CV_64FC1); //片方は回転、並進ともに0
      prjMat2 = cv::Mat(3, 4, CV_64FC1);
      for (int i = 0; i < 3; ++i)
	for (int j = 0; j < 3; ++j)
	  {
	    prjMat2.at<double>(i, j) = r.at<double>(i, j);
	  }
      prjMat2.at<double>(0, 3) = t.at<double>(0);
      prjMat2.at<double>(1, 3) = t.at<double>(1);
      prjMat2.at<double>(2, 3) = t.at<double>(2);

      std::cout << "Projection Matrix 1:\n" << prjMat1 << std::endl;
      std::cout << "Projection Matrix 2:\n" << prjMat2 << std::endl;

      //三角測量による三次元位置の推定
      cv::Mat point3D;
      cv::triangulatePoints(prjMat1, prjMat2, p1, p2, point3D);

      std::ofstream ofs( "points.txt" );
      for (int i = 0; i < point3D.cols; ++i)
	{
	  //誤対応以外の点を保存
	  if (mask.at<unsigned char>(i) > 0)
	    {
	      //色情報を取得
	      cv::Vec3b rgb = img1.at<cv::Vec3b>( keypoints1[dmatch[i].queryIdx].pt );
	      ofs << point3D.at<double>(0, i)/point3D.at<double>(3, i) << " " << point3D.at<double>(1, i)/point3D.at<double>(3, i) << " " << point3D.at<double>(2, i)/point3D.at<double>(3, i) << " " << (int)rgb[0] << " " << (int)rgb[1] << " " << (int)rgb[2] << std::endl;
	    }
	}
      ofs.close();
    }
  return 0;
}
