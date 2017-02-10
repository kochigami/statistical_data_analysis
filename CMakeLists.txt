cmake_minimum_required(VERSION 2.8.3)
project(my_tutorial)

find_package(catkin REQUIRED)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES walk_together
#  CATKIN_DEPENDS jsk_pepper_startup peppereus
#  DEPENDS system_lib
)

install(DIRECTORY euslisp
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
 )

