import rospy
import tf2_ros
import time
import copy
from geometry_msgs.msg import Vector3
from geometry_msgs.msg import PointStamped, Point
from tf2_geometry_msgs import do_transform_point

class TowerToWorld:
	def __init__(self, tower_goal=None):
		self.tower_goal = tower_goal


	def transform(self):
		# TODO: Instantiate the Buffer and TransformListener
		self.tfBuffer = tf2_ros.Buffer()
		self.listener = tf2_ros.TransformListener(self.tfBuffer)

		transform = self.tfBuffer.lookup_transform('world', 'tower', rospy.Time())
        # lookup_transform arguments are target_frame, source_frame, and time

        #TODO: Convert the goal to a PointStamped
        point = PointStamped(header=None, point=Point(x=self.tower_goal.x, y=self.tower_goal.y, z=self.tower_goal.z))

        #TODO: Use the do_transform_point function to convert the point using the transform
        new_point = do_transform_point(point, transform)

        #TODO: Convert the point back into a vector message containing integers
        goal = Vector3(x=new_point.point.x, y=new_point.point.y, z=new_point.point.z)
        rospy.loginfo(str(rospy.get_name()) + ": Transformed Goal From Tower to World {}".format([goal.x, goal.y]))

