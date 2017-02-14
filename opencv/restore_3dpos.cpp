#include <iostream>
#include <vector>
#include <fstream>
#include <opencv2/core.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/objdetect.hpp>
#include <opencv2/features2d.hpp>
#include <opencv2/calib3d.hpp>

using namespace cv;
using namespace std;

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
  Mat img1; //入力画像1
  Mat img2; //入力画像2
  Mat cameraMatrix;
  Mat distCoeffs;

  cameraMatrix = (Mat_<double>(3,3) << 554.925965, 0.000000, 322.448605, 0.000000, 560.790573, 264.018102, 0.000000, 0.000000, 1.000000);
  //distCoeffs = Mat_<double>(1,5) << 0.081784, -0.713658, 0.028528, 0.002789, 0.000000;
  distCoeffs = (cv::Mat_<double>(1,5) << 0.081784, -0.713658, 0.028528, 0.002789, 0.000000);
  
  cout << cameraMatrix << endl;
  cout << distCoeffs << endl;
  
  //cv::FileStorage fs("camera.xml", CV_STORAGE_READ);
  //fs["intrinsicMat"] >> cameraMatrix;
  //fs["distCoeffs"] >> distCoeffs;
  
  undistort(imread("/home/kochigami/Desktop/img1.png"), img1, cameraMatrix, distCoeffs);
  undistort(imread("/home/kochigami/Desktop/img2.png"), img2, cameraMatrix, distCoeffs);
  cout << "a" << endl;

  
  //cv::namedWindow("TEST1", CV_WINDOW_AUTOSIZE|CV_WINDOW_FREERATIO);
  //cv::imshow("TEST1", img1);
  //cv::namedWindow("TEST2", CV_WINDOW_AUTOSIZE|CV_WINDOW_FREERATIO);
  //cv::imshow("TEST2", img2);
  //cv::waitKey(0);
  
  //特徴抽出
  Ptr<Feature2D> detector1 = ORB::create();
  Ptr<Feature2D> detector2 = ORB::create();
  
  vector<cv::KeyPoint> keypoints1, keypoints2;
  Mat descriptors1, descriptors2;
  
  detector1->detectAndCompute( img1, Mat(), keypoints1, descriptors1);
  detector2->detectAndCompute( img2, Mat(), keypoints2, descriptors2);

  cout << descriptors1 << endl;
  cout << descriptors2 << endl;
  //cv::OrbFeatureDetector detector(300);
  //cv::OrbDescriptorExtractor descriptorExtractor;
  //detector.detect(img1, keypoints1);
  //descriptorExtractor.compute(img1, keypoints1, descriptor1);
  //detector.detect(img2, keypoints2);
  //descriptorExtractor.compute(img2, keypoints2, descriptor2);
  
  //cv::Ptr<cv::FeatureDetector> detector = cv::FeatureDetector::create( "SURF" ); //検出器
  //cv::Ptr<cv::DescriptorExtractor> descriptorExtractor = cv::DescriptorExtractor::create( "SURF" ); //特徴量
  
  //Ptr<DescriptorMatcher> matcher = DescriptorMatcher::create("BruteForce"); //対応点探索方法の設定

  //対応点の探索
  vector<DMatch> dmatch;
  vector<DMatch> dmatch12, dmatch21;

  BFMatcher matcher(NORM_HAMMING, false);
  matcher.match(descriptors1, descriptors2, dmatch12);
  matcher.match(descriptors2, descriptors1, dmatch21);
  
  //matcher->match(descriptor1, descriptor2, dmatch12); //img1 -> img2
  //matcher->match(descriptor2, descriptor1, dmatch21); //img2 -> img1
  
  for (size_t i = 0; i < dmatch12.size(); ++i)
    {
      //img1 -> img2 と img2 -> img1の結果が一致しているか検証
      DMatch m12 = dmatch12[i];
      DMatch m21 = dmatch21[m12.trainIdx];

      if (m21.trainIdx == m12.queryIdx)
	dmatch.push_back( m12 );
    }
  cout << dmatch12.size() << endl;
  cout << dmatch21.size() << endl;
  cout << dmatch.size() << endl;
  //十分な数の対応点があれば基礎行列を推定
  if (dmatch.size() > 5)
    {
      vector<Point2d> p1;
      vector<Point2d> p2;
      //対応付いた特徴点の取り出しと焦点距離1.0のときの座標に変換
      for (size_t i = 0; i < dmatch.size(); ++i)
	{
	  Mat ip(3, 1, CV_64FC1);
	  Point2d p;

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
      cout << "tmp2" << endl;
      
      Mat mask; //RANSACの結果を保持するためのマスク
      Mat essentialMat = findEssentialMat(p1, p2, 1.0, Point2f(0, 0), RANSAC, 0.9999, 0.003, mask);
      //cv::Mat essentialMat = cv::findEssentialMat(p1, p2);
      cout << "Essential Matrix\n" << essentialMat << endl;
      
      Mat r, t;
      recoverPose(essentialMat, p1, p2, r, t);
      cout << "R:\n" << r << endl;
      cout << "t:\n" << t << endl;
    
      Mat prjMat1, prjMat2;
      prjMat1 = Mat::eye(3, 4, CV_64FC1); //片方は回転、並進ともに0
      prjMat2 = Mat(3, 4, CV_64FC1);
      for (int i = 0; i < 3; ++i)
	for (int j = 0; j < 3; ++j)
	  {
	    prjMat2.at<double>(i, j) = r.at<double>(i, j);
	  }
      prjMat2.at<double>(0, 3) = t.at<double>(0);
      prjMat2.at<double>(1, 3) = t.at<double>(1);
      prjMat2.at<double>(2, 3) = t.at<double>(2);

      cout << "Projection Matrix 1:\n" << prjMat1 << endl;
      cout << "Projection Matrix 2:\n" << prjMat2 << endl;

      //三角測量による三次元位置の推定
      Mat point3D;
      triangulatePoints(prjMat1, prjMat2, p1, p2, point3D);
      cout << "d" << endl;
      ofstream ofs( "points.txt" );
      for (int i = 0; i < point3D.cols; ++i)
	{
	  //誤対応以外の点を保存
	  if (mask.at<unsigned char>(i) > 0)
	    {
	      //色情報を取得
	      Vec3b rgb = img1.at<Vec3b>( keypoints1[dmatch[i].queryIdx].pt );
	      ofs << point3D.at<double>(0, i)/point3D.at<double>(3, i) << " " << point3D.at<double>(1, i)/point3D.at<double>(3, i) << " " << point3D.at<double>(2, i)/point3D.at<double>(3, i) << " " << (int)rgb[0] << " " << (int)rgb[1] << " " << (int)rgb[2] << endl;
	    }
	}
      cout << "e" << endl;
      ofs.close();
    }
  return 0;
}
