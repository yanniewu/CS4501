#!/usr/bin/env python
import rospy
import copy
import numpy as np
# from astar_class import AStarPlanner
from geometry_msgs.msg import Vector3
from std_msgs.msg import Int32MultiArray
from std_msgs.msg import Int32
from std_msgs.msg import Bool
from geometry_msgs.msg import Point
from nav_msgs.msg import OccupancyGrid
from geometry_msgs.msg import PoseStamped
from sensor_msgs.msg import LaserScan
from environment_controller.srv import *
import time
import math

# Create a class which we will use to take keyboard commands and convert them to a position
class GlobalPlanner():
  # On node initialization
  def __init__(self):

    # Publisher and subscribers
    self.goal_sub = rospy.Subscriber("/cell_tower/position", Vector3, self.get_goal)
    self.lidar_sub = rospy.Subscriber("/uav/sensors/lidar", LaserScan, self.get_lidar)
    self.keys_left = rospy.Subscriber("/keys_remaining", Int32, self.get_keys)
    self.position_sub = rospy.Subscriber('/uav/sensors/gps', PoseStamped, self.get_position, queue_size = 1)
    self.map_pub = rospy.Publisher("/map", OccupancyGrid, queue_size=1)
    self.position_pub = rospy.Publisher("/uav/input/position", Vector3, queue_size=1)

    self.service = rospy.ServiceProxy('use_key', use_key)

    # Initialize class variables
    self.drone_position = []
    self.goal_position = []

    self.keys = 0
    self.door = Point()
    self.door_detected = True
    # set to false after checkpoint
    # self.door_detected = False

    # Initialize Occupancy Grid
    self.map = OccupancyGrid()
    self.map.info.resolution = 1
    self.map.info.width = rospy.get_param('/environment_controller/map_width')
    self.map.info.height = rospy.get_param('/environment_controller/map_height')
    self.map.info.origin.position.x = -(float(self.map.info.width)/2.0)
    self.map.info.origin.position.y = -(float(self.map.info.height)/2.0)
    self.map.data = [50]*(self.map.info.width*self.map.info.height)

    self.grid = np.reshape(self.map.data, (self.map.info.width, self.map.info.height))
    #rospy.loginfo(str(self.grid))
    # self.grid = []
    self.pub_map()

    self.lidar = LaserScan()
    self.mainloop()

  # Callback for gps subscriber
  def get_position(self, msg):
    self.drone_position = msg.pose.position
    self.update_map((0,0), 1)

  # Callback for tower subscriber
  def get_goal(self, msg):
      if len(self.goal_position) == 0:
        # get goal from tower
        x = int(round(msg.x, 0))
        y = int(round(msg.y, 0))

        self.goal_position = [x, y]
        rospy.loginfo(str(self.goal_position[0]) + ", " + str(self.goal_position[1]))
        # self.update_map((self.goal_position[0], self.goal_position[1]), -3)

  # Callback for key subscriber
  def get_keys(self, msg):
      # get number of keys remaining
      self.keys = msg.data

  # Callback for lidar subscriber
  def get_lidar(self, msg):
      # get lidar values to update occupancy grid
      self.lidar = msg

      up = self.lidar.ranges[3]
      #rospy.loginfo("up: " + str(up) + " ---- " + str(self.lidar.ranges[0]) + ", " + str(self.lidar.ranges[1]) + ", " + str(self.lidar.ranges[2]))
      left = self.lidar.ranges[7]
      down = self.lidar.ranges[11]
      right = self.lidar.ranges[15]

      #self.update_map((int(self.drone_position.x), int(self.drone_position.y)+5), 55)

      if math.isinf(up):
        up = self.lidar.range_max
      if math.isinf(down):
        down = self.lidar.range_max
      if math.isinf(left):
        left = self.lidar.range_max
      if math.isinf(right):
        right = self.lidar.range_max

      # UP
      self.update_map((int(self.drone_position.x), int(self.drone_position.y)+int(up)+1), 100)
      for i in range (1, int(up)+1):
        self.update_map((int(self.drone_position.x), int(self.drone_position.y)+i), 0)

      # DOWN
      self.update_map((int(self.drone_position.x), int(self.drone_position.y)-int(down)-1), 100)
      for i in range (1, int(down)+1):
        self.update_map((int(self.drone_position.x), int(self.drone_position.y)-i), 0)

      # LEFT
      self.update_map((int(self.drone_position.x)-int(left)-1, int(self.drone_position.y)), 100)
      for i in range (1, int(left)+1):
        self.update_map((int(self.drone_position.x)-i, int(self.drone_position.y)), 0)

      # RIGHT
      self.update_map((int(self.drone_position.x)+int(right)+1, int(self.drone_position.y)), 100)
      for i in range (1, int(right)+1):
        self.update_map((int(self.drone_position.x)+i, int(self.drone_position.y)), 0)


  # Uses key to open door and updates map
  def door_found(self):
    # comment this out after checkpoint 1, hardcoded door pos
    self.door.x = 1
    self.door.y = 0
    self.door.z = 0
    opened = self.service(self.door)
    if opened:
        self.update_map((self.door.x, self.door.y), -2)
    self.keys -= 1
    rospy.loginfo("Door at " + str(self.door.x) + ", " + str(self.door.y) + ", " + str(self.door.z) + ": " + str(opened))

  # Publishes map
  def pub_map(self):
    self.map.data = self.grid.flatten()
    # rospy.loginfo(str(self.grid))
    # rospy.loginfo(str(self.map.data))
    self.map_pub.publish(self.map)

  # Converts between occupancy grid and map
  def update_map(self, point, val):
    # 0, 0 in the occupancy grid is the top left corner which is -(width//2), height//2 in world
    # 1, 1 in world = 6, 6 in occupancy grid if 11x11 map
    #rospy.loginfo("point.x: " + str(point[0]) + ", " + "point.y: " + str(point[1]))

    x = point[0] + int(round(self.map.info.width*.5, 0)) - 1
    y = point[1] + int(round(self.map.info.height*.5, 0)) - 1

    #rospy.loginfo("x: " + str(x) + ", " + "y: " + str(y))

    # r, c (y, x) = new val
    if self.grid[x][y] not in set([-1,-2,-3]): # and (val > self.grid[x][y] and val != 1):
      self.grid[x][y] = val
    self.pub_map()

    # rospy.loginfo("x: " + str(x) + ", " + "y: " + str(y))


  def mainloop(self):
    # to update the occupancy grid from lidar data, need to transform by adding .5*width to the x val and .5*height to the y val
    # Set the rate of this loop
    rate = rospy.Rate(5)

    # future use code
    # rospy.loginfo(str(rospy.get_name()) + ": Executing path")
    # self.position_pub.publish(msg)

    # While ROS is still running
    while not rospy.is_shutdown():
      if self.door_detected and self.keys == 4:
          self.door_found()
          self.door_detected = False
      time.sleep(10)
      msg = Vector3(0, 3, 0)
      rospy.loginfo("Going through door")
      #self.position_pub.publish(msg)

      # Sleep for the remainder of the loop
      rate.sleep()


if __name__ == '__main__':
  rospy.init_node('global_planner')
  try:
    pp = GlobalPlanner()
  except rospy.ROSInterruptException:
    pass
