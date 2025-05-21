#!/usr/bin/env python
import rospy
import tf2_ros
import time
import copy
from geometry_msgs.msg import Vector3
from geometry_msgs.msg import PointStamped, Point
from tf2_geometry_msgs import do_transform_point

class TowerToMap:

  def __init__(self):
    time.sleep(10)
    # Used by the callback for the topic /tower/goal
    self.goal = None
    # TODO: Instantiate the Buffer and TransformListener
    self.tfBuffer = tf2_ros.Buffer()
    self.listener = tf2_ros.TransformListener(self.tfBuffer)

    # TODO: Goal publisher on topic /uav/input/goal
    self.position_pub = rospy.Publisher('/uav/input/goal', Vector3, queue_size=1)
    
    # TODO: Tower goal subscriber to topic /tower/goal
    self.tower_sub = rospy.Subscriber('/tower/goal', Vector3, self.getTowerGoal, queue_size=1)
    # start main loop
    self.mainloop()

  #TODO: Callback for the tower goal subscriber 
  def getTowerGoal(self, msg):
    # Save the keyboard command
    self.goal = msg

  def mainloop(self):
    # Set the rate of this loop
    rate = rospy.Rate(2)
    while not rospy.is_shutdown():
      if self.goal:
        try: 
          #TODO: Lookup the tower to world transform
          # lookup_transform arguments are target_frame, source_frame, and time
          transform = self.tfBuffer.lookup_transform('world', 'tower', rospy.Time())

          #TODO: Convert the goal to a PointStamped
          point = PointStamped(header=None, point=Point(x=self.goal.x, y=self.goal.y, z=self.goal.z))

          #TODO: Use the do_transform_point function to convert the point using the transform
          new_point = do_transform_point(point, transform)

          #TODO: Convert the point back into a vector message containing integers
          point = Vector3(x=new_point.point.x, y=new_point.point.y, z=new_point.point.z)

          #TODO: Publish the vector
          rospy.loginfo(str(rospy.get_name()) + ": Publishing Transformed Goal {}".format([point.x, point.y]))
          self.position_pub.publish(point)

          # The tower will automatically send you a new goal once the drone reaches the requested position.
          #TODO: Reset the goal
          self.goal = None

        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
          print('tf2 exception, continuing')
          continue
        
      rate.sleep()

if __name__ == '__main__':
  rospy.init_node('tower_to_map')
  try:
    tom = TowerToMap()
  except rospy.ROSInterruptException:
    pass