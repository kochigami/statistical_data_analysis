cmake_minimum_required(VERSION 2.8.3)
project(my_tutorial)

find_package(catkin REQUIRED
  cv_bridge
  image_transport
  roscpp
  rospy
  std_msgs
  sensor_msgs
  )

find_package(OpenCV REQUIRED)

catkin_package(
  #INCLUDE_DIRS include
  LIBRARIES ${PROJECT_NAME}
  CATKIN_DEPENDS rosconsole sensor_msgs
  DEPENDS OpenCV
  )

install(DIRECTORY
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
 )
include_directories(include ${OpenCV_INCLUDE_DIRS} ${catkin_INCLUDE_DIRS})
add_executable(face_detection src/face_detection.cpp)
target_link_libraries(face_detection ${OpenCV_LIBRARIES} ${catkin_LIBRARIES})