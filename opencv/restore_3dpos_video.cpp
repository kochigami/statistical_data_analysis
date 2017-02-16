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

int main(int argh, char* argv[])
{
  cv::VideoCapture cap(0);//デバイスのオープン
  vector<Point2d> pre_centers;
  cv::Mat pre_frame;
  
  if(!cap.isOpened())//カメラデバイスが正常にオープンしたか確認．
    {
      //読み込みに失敗したときの処理
      return -1;
    }

  while(1)//無限ループ
    {
      cv::Mat frame;
      cv::Point2d center;
      cv::Point2d pre_center;
	    
      vector<Point2d> centers;
      
      cap >> frame; // get a new frame from camera
      
      //カメラパラメータの読み込みとレンズ歪の除去
      Mat img1; //入力画像1
      Mat img2; //入力画像2
      Mat cameraMatrix;
      Mat distCoeffs;
      std::vector<cv::Rect> faces;
      std::vector<cv::Rect>::const_iterator f;
      
      cameraMatrix = (Mat_<double>(3,3) << 554.925965, 0.000000, 322.448605, 0.000000, 560.790573, 264.018102, 0.000000, 0.000000, 1.000000);
      distCoeffs = (cv::Mat_<double>(1,5) << 0.081784, -0.713658, 0.028528, 0.002789, 0.000000);
            
      undistort(frame, img1, cameraMatrix, distCoeffs);

      if (pre_frame.empty()){
	cap >> pre_frame;
      }
 
      undistort(pre_frame, img2, cameraMatrix, distCoeffs);
      //特徴抽出
      Ptr<Feature2D> detector1 = ORB::create();
      Ptr<Feature2D> detector2 = ORB::create();
      
      vector<cv::KeyPoint> keypoints1, keypoints2;
      Mat descriptors1, descriptors2;
	
      detector1->detectAndCompute( img1, Mat(), keypoints1, descriptors1);
      detector2->detectAndCompute( img2, Mat(), keypoints2, descriptors2);
	
      //対応点の探索
      vector<DMatch> dmatch;
      vector<DMatch> dmatch12, dmatch21;
	
      BFMatcher matcher(NORM_HAMMING, false);
      matcher.match(descriptors1, descriptors2, dmatch12);
      matcher.match(descriptors2, descriptors1, dmatch21);

      for (size_t i = 0; i < dmatch12.size(); ++i)
	{
	  //img1 -> img2 と img2 -> img1の結果が一致しているか検証
	  DMatch m12 = dmatch12[i];
	  DMatch m21 = dmatch21[m12.trainIdx];
	    
	  if (m21.trainIdx == m12.queryIdx)
	    dmatch.push_back( m12 );
	}
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
	    
	  Mat mask; //RANSACの結果を保持するためのマスク
	  Mat essentialMat = findEssentialMat(p1, p2, 1.0, Point2f(0, 0), RANSAC, 0.9999, 0.003, mask);
	  
	  Mat r, t;
	  recoverPose(essentialMat, p1, p2, r, t);
	    
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

	  double scale = 4.0;
	  cv::Mat gray, smallImg(cv::saturate_cast<int>(frame.rows/scale), cv::saturate_cast<int>(frame.cols/scale), CV_8UC1); // saturate_cast: transfer one type to another type
	  cv::cvtColor(frame, gray, CV_BGR2GRAY);
	  cv::resize(gray, smallImg, smallImg.size(), 0, 0, cv::INTER_LINEAR);
	  cv::equalizeHist(smallImg, smallImg); // equalize histgram (255)
	  
	  // Haar-like      
	  std::string cascadeName = "/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml";
	  cv::CascadeClassifier cascade;
	  if(!cascade.load(cascadeName))
	    return -1;
	  
	  /// マルチスケール（顔）探索
	  // 画像，出力矩形，縮小スケール，最低矩形数，（フラグ），最小矩形
	  cascade.detectMultiScale(smallImg, faces,
				   1.1, 2,
				   CV_HAAR_SCALE_IMAGE,
				   cv::Size(30, 30));

	  f = faces.begin();
	  for(; f != faces.end(); ++f) {
	    int radius;
	    center.x = cv::saturate_cast<int>((f->x + f->width*0.5)*scale);
	    center.y = cv::saturate_cast<int>((f->y + f->height*0.5)*scale);
	    radius = cv::saturate_cast<int>((f->width + f->height)*0.25*scale);
	    cv::circle(frame, center, radius, cv::Scalar(80,80,255), 3, 8, 0 );
	    centers.push_back(center);
	    // 0.25: 0.5 (average) * 0.5 (radius = half of dimension)
	  } //for
	  
	  
	  cv::imshow("window", frame);//画像を表示
	  cv::waitKey(1);

	  //三角測量による三次元位置の推定
	  Mat point3D;
	  if ((!pre_centers.empty() and !centers.empty()) and (pre_centers.size() == centers.size())) {
	    triangulatePoints(prjMat1, prjMat2, centers, pre_centers, point3D);
	    cout << point3D << endl;
	  }
	  
	  // clear pre_centers 
	  pre_centers.clear();
      
	  f = faces.begin();
	  for(; f != faces.end(); ++f){
	    pre_center.x = cv::saturate_cast<int>((f->x + f->width*0.5)*scale);
	    pre_center.y = cv::saturate_cast<int>((f->y + f->height*0.5)*scale);
	    pre_centers.push_back(pre_center);
	  }
	}
      cap >> pre_frame;
    }
  
  cv::destroyAllWindows();
  return 0;
}
