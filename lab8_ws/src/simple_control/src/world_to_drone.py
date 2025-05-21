#!/usr/bin/env python
import rospy
import tf2_ros
import time
import copy
import math
from geometry_msgs.msg import Vector3
from tf.transformations import quaternion_from_euler, euler_from_quaternion
from geometry_msgs.msg import PointStamped, PoseStamped, TransformStamped, Quaternion
from tf2_geometry_msgs import do_transform_point


class WorldToDrone:

    def __init__(self):
        time.sleep(10)
        # Used by the callback for the topic /tower/goal
        self.gps = None
        self.transform_stamped = TransformStamped()

        # TODO: Instantiate the Broadcaster
        self.br = tf2_ros.TransformBroadcaster()

        # TODO: Drone GPS subscriber to topic /uav/sensors/gps
        self.gps_sub = rospy.Subscriber('/uav/sensors/gps', PoseStamped, self.getPosition, queue_size = 1)


        # TODO: fill in the parent and child frames
        self.transform_stamped.header.frame_id = 'world'
        self.transform_stamped.child_frame_id = 'drone'

        # start main loop
        self.mainloop()

    # TODO: Callback for the GPS
    def getPosition(self, msg):
    # Save the keyboard command
        self.gps = msg


    def mainloop(self):
        # Set the rate of this loop
        rate = rospy.Rate(2)
        while not rospy.is_shutdown():
            if self.gps:

                # TODO: Use the GPS position to set up the transform
                self.transform_stamped.transform.translation = self.gps.pose.position  # TODO: set the Translation from the GPS
                roll, pitch, yaw = euler_from_quaternion((self.gps.pose.orientation.x, self.gps.pose.orientation.y, self.gps.pose.orientation.z, self.gps.pose.orientation.w))
                x,y,z,w = quaternion_from_euler(0, 0, yaw)
             
                self.transform_stamped.transform.rotation = Quaternion(x, y, z, w)  # TODO: set the quaternion from the GPS

                # TODO: Update the header to the current timestamp
                self.transform_stamped.header.stamp = rospy.Time() # TODO: set to the current time
                # TODO: Broadcast the transform
                self.br.sendTransform(self.transform_stamped)

            rate.sleep()


if __name__ == '__main__':
    rospy.init_node('world_to_drone')
    try:
        wod = WorldToDrone()
    except rospy.ROSInterruptException:
        pass