#!/usr/bin/env python
import rospy
import time
import math
import numpy as np
from threading import Lock

from geometry_msgs.msg import Vector3, PoseStamped, TwistStamped, Vector3Stamped
from std_msgs.msg import String, Bool, Float64
from sensor_msgs.msg import Image
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

from velocity_pid_class import PID

# A class used to follow ship below drone
class ShipFollower():
  # On node initialization
  def __init__(self):

    self.gps_z = 0
    self.gps_x = 0
    self.gps_y = 0
    self.beacon1_x = 0
    self.beacon1_y = 0
    self.beacon2_x = None
    self.beacon2_y = None

    # Allow the simulator to start
    time.sleep(3)

    # When this node shutsdown
    rospy.on_shutdown(self.shutdown_sequence)

    # TODO: Retrieve rate from ROS params
    self.rate = rospy.get_param("/ship_following_controller_node/rate", 4.0)
    self.dt = 1.0 / self.rate


    # TODO: Retrieve the PID parameters from ROS parameters
    self.pz = rospy.get_param("/ship_following_controller_node/pz", 0.2)
    self.iz = rospy.get_param("/ship_following_controller_node/iz", 0)
    self.dz =  rospy.get_param("/ship_following_controller_node/dz", 0)

    self.pxy = rospy.get_param("/ship_following_controller_node/pxy", 0.001)
    self.ixy = rospy.get_param("/ship_following_controller_node/ixy", 0)
    self.dxy = rospy.get_param("/ship_following_controller_node/dxy", 0)

    # TODO: Initialize PIDs with PID class and ROS parameters
    self.xy_pid = PID(p=self.pxy, i=self.ixy, d=self.dxy)
    self.z_pid = PID(p=self.pz, i=self.iz, d=self.dz)

    # TODO: Initialize zero'ed class vars
    self.last_time = rospy.Time.now()
    self.velocity = Vector3()
    self.est_pos = Vector3()

    # TODO: Create the publishers and subscribers
    self.gps_sub = rospy.Subscriber("uav/sensors/gps", PoseStamped, self.get_gps)
    self.beacon1_sub = rospy.Subscriber('/ship/beacon1', Vector3Stamped, self.get_ship_beacon1)
    self.beacon2_sub = rospy.Subscriber('/ship/beacon2', Vector3Stamped, self.get_ship_beacon2)
    self.velocity_pub = rospy.Publisher('/uav/input/velocityPID', Vector3, queue_size=1)
    self.est_pub = rospy.Publisher('/ship/estimated_position', Vector3, queue_size=1)

    # Run the control loop
    self.ControlLoop()

  # TODO FOR CHECKPOINT 1
  def get_gps(self, msg):
    # ONLY SAVE THE HEIGHT
    self.gps_z = msg.pose.position.z
    self.gps_x = msg.pose.position.x
    self.gps_y = msg.pose.position.y

  # TODO FOR CHECKPOINT 2
  # callback for /ship/beacon1
  def get_ship_beacon1(self, msg):
    self.beacon1_x = msg.vector.x
    self.beacon1_y = msg.vector.y

  # TODO FOR CHECKPOINT 2
  # callback for /ship/beacon2
  def get_ship_beacon2(self, msg):
    self.beacon2_x = msg.vector.x
    self.beacon2_y = msg.vector.y


  # TODO FOR CHECKPOINT 3
  # combine PID output from the two beacons
  # You don't have to use this method,
  # but you will need to use both error terms
  def combine_beacons(self):
    if self.beacon2_x == None:
      self.velocity.x = self.xy_pid.pid_loop(self.beacon1_x - self.gps_x, self.dt)
      self.velocity.y = self.xy_pid.pid_loop(self.beacon1_y - self.gps_y, self.dt)
    else:
      self.velocity.x = self.xy_pid.pid_loop(self.beacon2_x - self.gps_x, self.dt)
      self.velocity.y = self.xy_pid.pid_loop(self.beacon2_y - self.gps_y, self.dt)


  # This is the main loop of this class
  def ControlLoop(self):
    # Set the rate
    rate = rospy.Rate(self.rate)

    # While running
    while not rospy.is_shutdown():
      # Use PIDs to calculate the velocities you want

      # TODO FOR CHECKPOINT 1: z velocity
      self.velocity.z = self.z_pid.pid_loop(13 - self.gps_z, self.dt)

      # TODO FOR CHECKPOINT 2: x and y velocity
      self.combine_beacons()

      # publish velocity
      self.velocity_pub.publish(self.velocity)

      self.est_pos.x = self.gps_x + self.velocity.x
      self.est_pos.y = self.gps_y + self.velocity.y
      self.est_pos.z = self.gps_z + self.velocity.z

      self.est_pub.publish(self.est_pos)


      # Sleep any excess time
      rate.sleep()

  # Called on ROS shutdown
  def shutdown_sequence(self):
    rospy.loginfo(str(rospy.get_name()) + ": Shutting Down")


if __name__ == '__main__':
  rospy.init_node('ship_following_controller_node')
  try:
    ktp = ShipFollower()
  except rospy.ROSInterruptException:
    pass
