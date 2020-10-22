execute_process(COMMAND "/home/rob/Desktop/repo/SeniorDesign/ROB/stormBot_ws/build/diff_drive/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/rob/Desktop/repo/SeniorDesign/ROB/stormBot_ws/build/diff_drive/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
