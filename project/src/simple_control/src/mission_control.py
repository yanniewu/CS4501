#!/usr/bin/env python
import rospy
import copy
import numpy as np
from geometry_msgs.msg import Vector3
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Int32MultiArray, Int32
from std_msgs.msg import Bool
from nav_msgs.msg import OccupancyGrid

class MissionControl():
	def __init__(self):
		self.lidar_sub = rospy.Subscriber("/uav/sensors/lidar", LaserScan, self.get_lidar, queue_size=1)
		self.key_sub = rospy.Subscriber("keys_remaining", Int32, self.get_keys, queue_size=1)

		self.num_keys = 0

		self.mainloop()

	def get_lidar(self, msg):
		pass

	def get_keys(self, msg):
		self.num_keys = msg.data



	# The main loop of the function
  	def mainloop(self):
  		# Set the rate of this loop
  		rate = rospy.Rate(20)

    	# While ROS is still running
    	while not rospy.is_shutdown():

      		# Sleep for the remainder of the loop
      		rate.sleep()

if __name__ == '__main__':
  rospy.init_node('mission_control_node')
  try:
    mc = MissionControl()
  except rospy.ROSInterruptException:
    pass