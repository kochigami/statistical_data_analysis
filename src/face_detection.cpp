#include <ros/ros.h>
#include <image_transport/image_transport.h>
#include <cv_bridge/cv_bridge.h>
#include <sensor_msgs/image_encodings.h>
#include <opencv2/core/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/objdetect/objdetect.hpp>
#include <opencv2/highgui/highgui.hpp>

static const std::string OPENCV_WINDOW = "Image window";

class ImageConverter
{
  ros::NodeHandle nh_;
  image_transport::ImageTransport it_;
  image_transport::Subscriber image_sub_;
  image_transport::Publisher image_pub_;
  
public:
  ImageConverter()
    : it_(nh_)
  {
    // Subscrive to input video feed and publish output video feed
    image_sub_ = it_.subscribe("/camera/rgb/image_raw", 1, 
			       &ImageConverter::imageCb, this);
    image_pub_ = it_.advertise("/image_converter/output_video", 1);
    cv::namedWindow(OPENCV_WINDOW);
  }

  ~ImageConverter()
  {
    cv::destroyWindow(OPENCV_WINDOW);
  }

  void imageCb(const sensor_msgs::ImageConstPtr& msg)
  {
    cv_bridge::CvImagePtr cv_ptr;
    try
      {
	cv_ptr = cv_bridge::toCvCopy(msg, sensor_msgs::image_encodings::BGR8);
      }
    catch (cv_bridge::Exception& e)
      {
	ROS_ERROR("cv_bridge exception: %s", e.what());
	return;
      }

    double scale = 4.0;
    cv::Mat gray, smallImg(cv::saturate_cast<int>(cv_ptr->image.rows/scale), cv::saturate_cast<int>(cv_ptr->image.cols/scale), CV_8UC1); // saturate_cast: transfer one type to another type
    cv::cvtColor(cv_ptr->image, gray, CV_BGR2GRAY);
    cv::resize(gray, smallImg, smallImg.size(), 0, 0, cv::INTER_LINEAR);
    cv::equalizeHist(smallImg, smallImg); // equalize histgram (255)
    
    // Haar-like      
    std::string cascadeName = "/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml";
    cv::CascadeClassifier cascade;
    if(!cascade.load(cascadeName))
      return;
    
    std::vector<cv::Rect> faces;
    /// マルチスケール（顔）探索
    // 画像，出力矩形，縮小スケール，最低矩形数，（フラグ），最小矩形
    cascade.detectMultiScale(smallImg, faces,
			     1.1, 2,
			     CV_HAAR_SCALE_IMAGE,
			     cv::Size(30, 30));
    
    std::vector<cv::Rect>::const_iterator r = faces.begin();
    for(; r != faces.end(); ++r) {
      cv::Point center;
      int radius;
      center.x = cv::saturate_cast<int>((r->x + r->width*0.5)*scale);
      center.y = cv::saturate_cast<int>((r->y + r->height*0.5)*scale);
      radius = cv::saturate_cast<int>((r->width + r->height)*0.25*scale); // 0.25: 0.5 (average) * 0.5 (radius = half of dimension)
      cv::circle(cv_ptr->image, center, radius, cv::Scalar(80,80,255), 3, 8, 0 );
    }
    
    //cv::namedWindow("result", CV_WINDOW_AUTOSIZE|CV_WINDOW_FREERATIO);
    cv::imshow(OPENCV_WINDOW, cv_ptr->image);
    cv::waitKey(3);
    

    // Update GUI Window
    //cv::imshow(OPENCV_WINDOW, cv_ptr->image);
    //cv::waitKey(3);
    
    // Output modified video stream
    image_pub_.publish(cv_ptr->toImageMsg());
  }
};

int main(int argc, char** argv)
{
  ros::init(argc, argv, "image_converter");
  ImageConverter ic;
  ros::spin();
  return 0;
}
