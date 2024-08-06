cmake_minimum_required(VERSION 3.0.2)
project(drone_navigation)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  sensor_msgs
  nav_msgs
  cv_bridge
)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS
  src/slam_node.py
  src/obstacle_detection.py
  src/autonomous_navigation.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
