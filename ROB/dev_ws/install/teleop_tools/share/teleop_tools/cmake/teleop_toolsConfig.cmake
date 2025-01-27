# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_teleop_tools_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED teleop_tools_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(teleop_tools_FOUND FALSE)
  elseif(NOT teleop_tools_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(teleop_tools_FOUND FALSE)
  endif()
  return()
endif()
set(_teleop_tools_CONFIG_INCLUDED TRUE)

# output package information
if(NOT teleop_tools_FIND_QUIETLY)
  message(STATUS "Found teleop_tools: 1.1.0 (${teleop_tools_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'teleop_tools' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  message(WARNING "${_msg}")
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(teleop_tools_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${teleop_tools_DIR}/${_extra}")
endforeach()
