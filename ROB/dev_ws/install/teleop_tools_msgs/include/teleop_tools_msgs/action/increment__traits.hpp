// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from teleop_tools_msgs:action/Increment.idl
// generated code does not contain a copyright notice

#ifndef TELEOP_TOOLS_MSGS__ACTION__INCREMENT__TRAITS_HPP_
#define TELEOP_TOOLS_MSGS__ACTION__INCREMENT__TRAITS_HPP_

#include "teleop_tools_msgs/action/increment__struct.hpp"
#include <rosidl_generator_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<teleop_tools_msgs::action::Increment_Goal>()
{
  return "teleop_tools_msgs::action::Increment_Goal";
}

template<>
struct has_fixed_size<teleop_tools_msgs::action::Increment_Goal>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<teleop_tools_msgs::action::Increment_Goal>
  : std::integral_constant<bool, false> {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<teleop_tools_msgs::action::Increment_Result>()
{
  return "teleop_tools_msgs::action::Increment_Result";
}

template<>
struct has_fixed_size<teleop_tools_msgs::action::Increment_Result>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<teleop_tools_msgs::action::Increment_Result>
  : std::integral_constant<bool, true> {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<teleop_tools_msgs::action::Increment_Feedback>()
{
  return "teleop_tools_msgs::action::Increment_Feedback";
}

template<>
struct has_fixed_size<teleop_tools_msgs::action::Increment_Feedback>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<teleop_tools_msgs::action::Increment_Feedback>
  : std::integral_constant<bool, true> {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/uuid__traits.hpp"
// Member 'goal'
#include "teleop_tools_msgs/action/increment__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<teleop_tools_msgs::action::Increment_SendGoal_Request>()
{
  return "teleop_tools_msgs::action::Increment_SendGoal_Request";
}

template<>
struct has_fixed_size<teleop_tools_msgs::action::Increment_SendGoal_Request>
  : std::integral_constant<bool, has_fixed_size<teleop_tools_msgs::action::Increment_Goal>::value && has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<teleop_tools_msgs::action::Increment_SendGoal_Request>
  : std::integral_constant<bool, has_bounded_size<teleop_tools_msgs::action::Increment_Goal>::value && has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/time__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<teleop_tools_msgs::action::Increment_SendGoal_Response>()
{
  return "teleop_tools_msgs::action::Increment_SendGoal_Response";
}

template<>
struct has_fixed_size<teleop_tools_msgs::action::Increment_SendGoal_Response>
  : std::integral_constant<bool, has_fixed_size<builtin_interfaces::msg::Time>::value> {};

template<>
struct has_bounded_size<teleop_tools_msgs::action::Increment_SendGoal_Response>
  : std::integral_constant<bool, has_bounded_size<builtin_interfaces::msg::Time>::value> {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<teleop_tools_msgs::action::Increment_SendGoal>()
{
  return "teleop_tools_msgs::action::Increment_SendGoal";
}

template<>
struct has_fixed_size<teleop_tools_msgs::action::Increment_SendGoal>
  : std::integral_constant<
    bool,
    has_fixed_size<teleop_tools_msgs::action::Increment_SendGoal_Request>::value &&
    has_fixed_size<teleop_tools_msgs::action::Increment_SendGoal_Response>::value
  >
{
};

template<>
struct has_bounded_size<teleop_tools_msgs::action::Increment_SendGoal>
  : std::integral_constant<
    bool,
    has_bounded_size<teleop_tools_msgs::action::Increment_SendGoal_Request>::value &&
    has_bounded_size<teleop_tools_msgs::action::Increment_SendGoal_Response>::value
  >
{
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/uuid__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<teleop_tools_msgs::action::Increment_GetResult_Request>()
{
  return "teleop_tools_msgs::action::Increment_GetResult_Request";
}

template<>
struct has_fixed_size<teleop_tools_msgs::action::Increment_GetResult_Request>
  : std::integral_constant<bool, has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<teleop_tools_msgs::action::Increment_GetResult_Request>
  : std::integral_constant<bool, has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'result'
// already included above
// #include "teleop_tools_msgs/action/increment__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<teleop_tools_msgs::action::Increment_GetResult_Response>()
{
  return "teleop_tools_msgs::action::Increment_GetResult_Response";
}

template<>
struct has_fixed_size<teleop_tools_msgs::action::Increment_GetResult_Response>
  : std::integral_constant<bool, has_fixed_size<teleop_tools_msgs::action::Increment_Result>::value> {};

template<>
struct has_bounded_size<teleop_tools_msgs::action::Increment_GetResult_Response>
  : std::integral_constant<bool, has_bounded_size<teleop_tools_msgs::action::Increment_Result>::value> {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<teleop_tools_msgs::action::Increment_GetResult>()
{
  return "teleop_tools_msgs::action::Increment_GetResult";
}

template<>
struct has_fixed_size<teleop_tools_msgs::action::Increment_GetResult>
  : std::integral_constant<
    bool,
    has_fixed_size<teleop_tools_msgs::action::Increment_GetResult_Request>::value &&
    has_fixed_size<teleop_tools_msgs::action::Increment_GetResult_Response>::value
  >
{
};

template<>
struct has_bounded_size<teleop_tools_msgs::action::Increment_GetResult>
  : std::integral_constant<
    bool,
    has_bounded_size<teleop_tools_msgs::action::Increment_GetResult_Request>::value &&
    has_bounded_size<teleop_tools_msgs::action::Increment_GetResult_Response>::value
  >
{
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/uuid__traits.hpp"
// Member 'feedback'
// already included above
// #include "teleop_tools_msgs/action/increment__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<teleop_tools_msgs::action::Increment_FeedbackMessage>()
{
  return "teleop_tools_msgs::action::Increment_FeedbackMessage";
}

template<>
struct has_fixed_size<teleop_tools_msgs::action::Increment_FeedbackMessage>
  : std::integral_constant<bool, has_fixed_size<teleop_tools_msgs::action::Increment_Feedback>::value && has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<teleop_tools_msgs::action::Increment_FeedbackMessage>
  : std::integral_constant<bool, has_bounded_size<teleop_tools_msgs::action::Increment_Feedback>::value && has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

}  // namespace rosidl_generator_traits

#endif  // TELEOP_TOOLS_MSGS__ACTION__INCREMENT__TRAITS_HPP_
