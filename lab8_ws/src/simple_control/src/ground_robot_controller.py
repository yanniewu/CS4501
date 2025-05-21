#!/usr/bin/env python
import rospy
import tf2_ros
import time
import copy
from geometry_msgs.msg import Vector3
from geometry_msgs.msg import PointStamped, Point
from tf2_geometry_msgs import do_transform_point


class GroundRobotController:

    def __init__(self):
        time.sleep(20)  # takes longer for the other items to come up
        # Our goal is 0,0,0 *in the drone frame*
        self.goal = Vector3()
        # TODO: Instantiate the Buffer and TransformListener
        self.tfBuffer = tf2_ros.Buffer()
        self.listener = tf2_ros.TransformListener(self.tfBuffer)

        # TODO: set up publisher to /ground_robot/goal - this will publish *in the world frame*
        self.position_pub = rospy.Publisher('/ground_robot/goal', Vector3, queue_size=1)

        # start main loop
        self.mainloop()


    def mainloop(self):
        # Set the rate of this loop
        rate = rospy.Rate(2)
        while not rospy.is_shutdown():
            if self.goal:

                try:
                    # TODO: Lookup the drone to world transform
                    transform = self.tfBuffer.lookup_transform('drone', 'world', rospy.Time())

                    # TODO: Convert the goal to a PointStamped
                    point = PointStamped(header=None, point=Point(x=self.goal.x, y=self.goal.y, z=self.goal.z))

                    # TODO: Use the do_transform_point function to convert the point using the transform
                    new_point = do_transform_point(point, transform)

                    # TODO: Convert the point back into a vector message containing integers
                    point = Vector3(x=new_point.point.x, y=new_point.point.y, z=new_point.point.z)

                    # TODO: Publish the vector
                    rospy.loginfo(str(rospy.get_name()) + ": Publishing Transformed Goal {}".format([point.x, point.y]))
                    self.position_pub.publish(point)


                except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
                    continue

            rate.sleep()


if __name__ == '__main__':
    rospy.init_node('ground_robot_controller')
    try:
        tom = GroundRobotController()
    except rospy.ROSInterruptException:
        pass