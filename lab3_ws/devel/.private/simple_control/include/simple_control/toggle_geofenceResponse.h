// Generated by gencpp from file simple_control/toggle_geofenceResponse.msg
// DO NOT EDIT!


#ifndef SIMPLE_CONTROL_MESSAGE_TOGGLE_GEOFENCERESPONSE_H
#define SIMPLE_CONTROL_MESSAGE_TOGGLE_GEOFENCERESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace simple_control
{
template <class ContainerAllocator>
struct toggle_geofenceResponse_
{
  typedef toggle_geofenceResponse_<ContainerAllocator> Type;

  toggle_geofenceResponse_()
    : success(false)  {
    }
  toggle_geofenceResponse_(const ContainerAllocator& _alloc)
    : success(false)  {
  (void)_alloc;
    }



   typedef uint8_t _success_type;
  _success_type success;





  typedef boost::shared_ptr< ::simple_control::toggle_geofenceResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::simple_control::toggle_geofenceResponse_<ContainerAllocator> const> ConstPtr;

}; // struct toggle_geofenceResponse_

typedef ::simple_control::toggle_geofenceResponse_<std::allocator<void> > toggle_geofenceResponse;

typedef boost::shared_ptr< ::simple_control::toggle_geofenceResponse > toggle_geofenceResponsePtr;
typedef boost::shared_ptr< ::simple_control::toggle_geofenceResponse const> toggle_geofenceResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::simple_control::toggle_geofenceResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::simple_control::toggle_geofenceResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::simple_control::toggle_geofenceResponse_<ContainerAllocator1> & lhs, const ::simple_control::toggle_geofenceResponse_<ContainerAllocator2> & rhs)
{
  return lhs.success == rhs.success;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::simple_control::toggle_geofenceResponse_<ContainerAllocator1> & lhs, const ::simple_control::toggle_geofenceResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace simple_control

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::simple_control::toggle_geofenceResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::simple_control::toggle_geofenceResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::simple_control::toggle_geofenceResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::simple_control::toggle_geofenceResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::simple_control::toggle_geofenceResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::simple_control::toggle_geofenceResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::simple_control::toggle_geofenceResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "358e233cde0c8a8bcfea4ce193f8fc15";
  }

  static const char* value(const ::simple_control::toggle_geofenceResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x358e233cde0c8a8bULL;
  static const uint64_t static_value2 = 0xcfea4ce193f8fc15ULL;
};

template<class ContainerAllocator>
struct DataType< ::simple_control::toggle_geofenceResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "simple_control/toggle_geofenceResponse";
  }

  static const char* value(const ::simple_control::toggle_geofenceResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::simple_control::toggle_geofenceResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool success\n"
"\n"
;
  }

  static const char* value(const ::simple_control::toggle_geofenceResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::simple_control::toggle_geofenceResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.success);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct toggle_geofenceResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::simple_control::toggle_geofenceResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::simple_control::toggle_geofenceResponse_<ContainerAllocator>& v)
  {
    s << indent << "success: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.success);
  }
};

} // namespace message_operations
} // namespace ros

#endif // SIMPLE_CONTROL_MESSAGE_TOGGLE_GEOFENCERESPONSE_H
