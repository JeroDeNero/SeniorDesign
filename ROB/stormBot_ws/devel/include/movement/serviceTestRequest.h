// Generated by gencpp from file movement/serviceTestRequest.msg
// DO NOT EDIT!


#ifndef MOVEMENT_MESSAGE_SERVICETESTREQUEST_H
#define MOVEMENT_MESSAGE_SERVICETESTREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace movement
{
template <class ContainerAllocator>
struct serviceTestRequest_
{
  typedef serviceTestRequest_<ContainerAllocator> Type;

  serviceTestRequest_()
    : a(0.0)
    , b(0.0)  {
    }
  serviceTestRequest_(const ContainerAllocator& _alloc)
    : a(0.0)
    , b(0.0)  {
  (void)_alloc;
    }



   typedef float _a_type;
  _a_type a;

   typedef float _b_type;
  _b_type b;





  typedef boost::shared_ptr< ::movement::serviceTestRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::movement::serviceTestRequest_<ContainerAllocator> const> ConstPtr;

}; // struct serviceTestRequest_

typedef ::movement::serviceTestRequest_<std::allocator<void> > serviceTestRequest;

typedef boost::shared_ptr< ::movement::serviceTestRequest > serviceTestRequestPtr;
typedef boost::shared_ptr< ::movement::serviceTestRequest const> serviceTestRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::movement::serviceTestRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::movement::serviceTestRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::movement::serviceTestRequest_<ContainerAllocator1> & lhs, const ::movement::serviceTestRequest_<ContainerAllocator2> & rhs)
{
  return lhs.a == rhs.a &&
    lhs.b == rhs.b;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::movement::serviceTestRequest_<ContainerAllocator1> & lhs, const ::movement::serviceTestRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace movement

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::movement::serviceTestRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::movement::serviceTestRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::movement::serviceTestRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::movement::serviceTestRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::movement::serviceTestRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::movement::serviceTestRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::movement::serviceTestRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "3f6326d24b4937f854196fd3a843f42e";
  }

  static const char* value(const ::movement::serviceTestRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x3f6326d24b4937f8ULL;
  static const uint64_t static_value2 = 0x54196fd3a843f42eULL;
};

template<class ContainerAllocator>
struct DataType< ::movement::serviceTestRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "movement/serviceTestRequest";
  }

  static const char* value(const ::movement::serviceTestRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::movement::serviceTestRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32 a\n"
"float32 b\n"
;
  }

  static const char* value(const ::movement::serviceTestRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::movement::serviceTestRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.a);
      stream.next(m.b);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct serviceTestRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::movement::serviceTestRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::movement::serviceTestRequest_<ContainerAllocator>& v)
  {
    s << indent << "a: ";
    Printer<float>::stream(s, indent + "  ", v.a);
    s << indent << "b: ";
    Printer<float>::stream(s, indent + "  ", v.b);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MOVEMENT_MESSAGE_SERVICETESTREQUEST_H
