#!/usr/bin/env python
# A class used to visit different waypoints on a map
import time
import rospy
import math
import numpy as np
from geometry_msgs.msg import Vector3, PoseStamped

class VisitWaypoints():
  # On node initialization
  def __init__(self):
    # Init the waypoints [x,y] pairs, we will later obtain them from the command line
    waypoints_str = rospy.get_param("/visit_waypoints_node/waypoints", "[[2,6],[2,-4],[-2,-2],[4,-2],[-5,5],[4,4],[-6,-6]]")
    # Convert from string to numpy array
    try:
      self.waypoints=waypoints_str.replace('[','')
      self.waypoints=self.waypoints.replace(']','')
      self.waypoints=np.fromstring(self.waypoints,dtype=int,sep=',')
      self.waypoints=np.reshape(self.waypoints, (-1, 2))
    except:
      print("Error: Could not convert waypoints to Numpy array")
      print(waypoints_str)
      exit()

    # Create the position message we are going to be sending
    self.pos = Vector3()
    self.pos.z = 2.0
    self.reachedAll = False

    # Keeps track of drone's current position
    self.current_position = np.zeros(3, dtype=np.float64)
    
    # TODO Checkpoint 1:
    # Subscribe to `uav/sensors/gps`
    self.gps_sub = rospy.Subscriber('uav/sensors/gps', PoseStamped, self.get_gps)
        

    # Create the publisher and subscriber
    self.position_pub = rospy.Publisher('/uav/input/position_request', Vector3, queue_size=1)

    # Call the mainloop of our class
    self.mainloop()

   # Call back to get the gps data
  def get_gps(self, msg):
    self.current_position[0] = msg.pose.position.x
    self.current_position[1] = msg.pose.position.y
    self.current_position[2] = msg.pose.position.z

 
  def mainloop(self):
    # Set the rate of this loop
    rate = rospy.Rate(1)

    # Wait 10 seconds before starting
    time.sleep(10)

    # TODO Checkpoint 1
    # Update mainloop() to fly between the different positions

    # While ROS is still running
    while not rospy.is_shutdown():
      # TODO Checkpoint 1
      # Check that we are at the waypoint for 5 seconds 
      # Publish the position
      if self.reachedAll!= True:
        isMoving = False
        
        for w in self.waypoints:
          rospy.loginfo("Going to waypoint.")
          self.pos.x = w[0]
          self.pos.y = w[1]
          self.position_pub.publish(self.pos)    
          isMoving = True
        
          while isMoving == True:
            dx = self.current_position[0] - w[0]
            dy = self.current_position[1] - w[1]
            distance_to_target = math.sqrt(pow(dx, 2) + pow(dy, 2))
          
            if distance_to_target < 0.5:
              rospy.loginfo("Reached waypoint; hovering for 5 seconds.")
              isMoving = False
              time.sleep(5)

        rospy.loginfo("Reached all waypoints.")
        self.reachedAll = True
      # Sleep for the remainder of the loop
      rate.sleep()


if __name__ == '__main__':
  rospy.init_node('visit_waypoints')
  try:
    ktp = VisitWaypoints()
  except rospy.ROSInterruptException:
    pass