#!/usr/bin/env python
import rospy
import time
import math
from geometry_msgs.msg import PointStamped
from altitude.msg import AltitudeStamped
from moving_average import MovingAverage

class LidarAltitudeMA:
    # Node initialization
    def __init__(self):

        # Create the publisher and subscriber
        self.pub = rospy.Publisher('/uav/sensors/lidar_altitude_ma', AltitudeStamped, queue_size=1) # Changed for CHECKPOINT 3
        self.moving_average = MovingAverage(10)
        self.sub = rospy.Subscriber('/uav/sensors/lidar_position', PointStamped, self.process_altitude, queue_size=1)
        
        self.gps_error = float(rospy.get_param('/uav/sensors/lidar_position_noise', str(0))) # Changed for CHECKPOINT 3
        self.altitude = AltitudeStamped()
        self.gps_pose = PointStamped()
        rospy.spin()

    def process_altitude(self, msg):
        self.gps_pose = msg
        self.moving_average.add(self.gps_pose.point.z)  
        self.altitude.value = self.moving_average.get_average()
        self.altitude.stamp = self.gps_pose.header.stamp
        self.altitude.error = self.gps_error/math.sqrt(self.moving_average.size)
        self.pub.publish(self.altitude)


if __name__ == '__main__':
    rospy.init_node('lidar_altitude_ma_node')
    try:
        LidarAltitudeMA()
    except rospy.ROSInterruptException:
        pass
