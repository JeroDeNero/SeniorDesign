# Install script for directory: /home/rob/Desktop/repo/SeniorDesign/ROB/stormBot_ws/src/diff_drive

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/rob/Desktop/repo/SeniorDesign/ROB/stormBot_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/diff_drive/action" TYPE FILE FILES "/home/rob/Desktop/repo/SeniorDesign/ROB/stormBot_ws/src/diff_drive/action/GoToPose.action")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/diff_drive/msg" TYPE FILE FILES
    "/home/rob/Desktop/repo/SeniorDesign/ROB/stormBot_ws/devel/share/diff_drive/msg/GoToPoseAction.msg"
    "/home/rob/Desktop/repo/SeniorDesign/ROB/stormBot_ws/devel/share/diff_drive/msg/GoToPoseActionGoal.msg"
    "/home/rob/Desktop/repo/SeniorDesign/ROB/stormBot_ws/devel/share/diff_drive/msg/GoToPoseActionResult.msg"
    "/home/rob/Desktop/repo/SeniorDesign/ROB/stormBot_ws/devel/share/diff_drive/msg/GoToPoseActionFeedback.msg"
    "/home/rob/Desktop/repo/SeniorDesign/ROB/stormBot_ws/devel/share/diff_drive/msg/GoToPoseGoal.msg"
    "/home/rob/Desktop/repo/SeniorDesign/ROB/stormBot_ws/devel/share/diff_drive/msg/GoToPoseResult.msg"
    "/home/rob/Desktop/repo/SeniorDesign/ROB/stormBot_ws/devel/share/diff_drive/msg/GoToPoseFeedback.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/diff_drive" TYPE PROGRAM FILES "/home/rob/Desktop/repo/SeniorDesign/ROB/stormBot_ws/build/diff_drive/catkin_generated/installspace/diff_drive_odometry")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/diff_drive" TYPE PROGRAM FILES "/home/rob/Desktop/repo/SeniorDesign/ROB/stormBot_ws/build/diff_drive/catkin_generated/installspace/diff_drive_controller")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/diff_drive" TYPE PROGRAM FILES "/home/rob/Desktop/repo/SeniorDesign/ROB/stormBot_ws/build/diff_drive/catkin_generated/installspace/diff_drive_go_to_goal")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/diff_drive" TYPE PROGRAM FILES "/home/rob/Desktop/repo/SeniorDesign/ROB/stormBot_ws/build/diff_drive/catkin_generated/installspace/diff_drive_mock_robot")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  include("/home/rob/Desktop/repo/SeniorDesign/ROB/stormBot_ws/build/diff_drive/catkin_generated/safe_execute_install.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/diff_drive/cmake" TYPE FILE FILES "/home/rob/Desktop/repo/SeniorDesign/ROB/stormBot_ws/build/diff_drive/catkin_generated/installspace/diff_drive-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/rob/Desktop/repo/SeniorDesign/ROB/stormBot_ws/devel/include/diff_drive")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/rob/Desktop/repo/SeniorDesign/ROB/stormBot_ws/devel/share/roseus/ros/diff_drive")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/rob/Desktop/repo/SeniorDesign/ROB/stormBot_ws/devel/share/common-lisp/ros/diff_drive")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/rob/Desktop/repo/SeniorDesign/ROB/stormBot_ws/devel/share/gennodejs/ros/diff_drive")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python2" -m compileall "/home/rob/Desktop/repo/SeniorDesign/ROB/stormBot_ws/devel/lib/python2.7/dist-packages/diff_drive")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/rob/Desktop/repo/SeniorDesign/ROB/stormBot_ws/devel/lib/python2.7/dist-packages/diff_drive" REGEX "/\\_\\_init\\_\\_\\.py$" EXCLUDE REGEX "/\\_\\_init\\_\\_\\.pyc$" EXCLUDE)
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/rob/Desktop/repo/SeniorDesign/ROB/stormBot_ws/devel/lib/python2.7/dist-packages/diff_drive" FILES_MATCHING REGEX "/home/rob/Desktop/repo/SeniorDesign/ROB/stormBot_ws/devel/lib/python2.7/dist-packages/diff_drive/.+/__init__.pyc?$")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/rob/Desktop/repo/SeniorDesign/ROB/stormBot_ws/build/diff_drive/catkin_generated/installspace/diff_drive.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/diff_drive/cmake" TYPE FILE FILES "/home/rob/Desktop/repo/SeniorDesign/ROB/stormBot_ws/build/diff_drive/catkin_generated/installspace/diff_drive-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/diff_drive/cmake" TYPE FILE FILES
    "/home/rob/Desktop/repo/SeniorDesign/ROB/stormBot_ws/build/diff_drive/catkin_generated/installspace/diff_driveConfig.cmake"
    "/home/rob/Desktop/repo/SeniorDesign/ROB/stormBot_ws/build/diff_drive/catkin_generated/installspace/diff_driveConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/diff_drive" TYPE FILE FILES "/home/rob/Desktop/repo/SeniorDesign/ROB/stormBot_ws/src/diff_drive/package.xml")
endif()

