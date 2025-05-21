#!/usr/bin/env python
import rospy
import time
import copy
from enum import Enum
from math import sqrt, pow
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Vector3
from geometry_msgs.msg import Point
from simple_control.srv import toggle_geofence, toggle_geofenceResponse


# A class to keep track of the quadrotors state
class DroneState(Enum):
  HOVERING = 1
  VERIFYING = 2
  MOVING = 3


# Create a class which takes in a position and verifies it, keeps track of the state and publishes commands to a drone
class GeofenceAndMission:

  # Node initialization
  def __init__(self):

    # Create the publisher and subscriber
    self.position_pub = rospy.Publisher('/uav/input/position', Vector3, queue_size=1)
    self.keyboard_sub = rospy.Subscriber('/keyboardmanager/position', Vector3, self.getKeyboardCommand, queue_size = 1)
    
    # TO BE COMPLETED FOR CHECKPOINT 2
    # TODO: Add a position_sub that subscribes to the drones pose
    self.position_sub = rospy.Subscriber('/uav/sensors/gps', PoseStamped, self.getDronePosition, queue_size = 1)

    # TO BE COMPLETED FOR CHECKPOINT 3
    # TODO: Get the geofence parameters
    # Get the acceptance range
    self.acceptance_range = rospy.get_param("/geofence_and_mission_node/acceptance_range", 0.25)

    # CHECKPOINT 5
    self.service = rospy.Service('toggle_geofence', toggle_geofence, self.toggleGeofence)
    self.geofence_on = True

    # Getting the geofence parameters
    geofence_params = rospy.get_param('/geofence_and_mission_node/geofence', {'x': 3, 'y': 3, 'z': 3})
    cx, cy, cz = geofence_params['x'], geofence_params['y'], geofence_params['z']

    # Create the geofence
    self.geofence_x = [-1 * cx, cx]
    self.geofence_y = [-1 * cy, cy]
    self.geofence_z = [0, cz]

    # Display incoming parameters
    rospy.loginfo(str(rospy.get_name()) + ": Launching with the following parameters:")
    rospy.loginfo(str(rospy.get_name()) + ": Param: geofence x - " + str(self.geofence_x))
    rospy.loginfo(str(rospy.get_name()) + ": Param: geofence y - " + str(self.geofence_y))
    rospy.loginfo(str(rospy.get_name()) + ": Param: geofence z - " + str(self.geofence_z))
    rospy.loginfo(str(rospy.get_name()) + ": Param: acceptance range - " + str(self.acceptance_range))

    # Create the drones state as hovering
    self.state = DroneState.HOVERING
    rospy.loginfo(str(rospy.get_name()) + ": Current State: HOVERING")
    # Create the goal messages we are going to be sending
    self.goal_cmd = Vector3()

    # Create a point message that saves the drones current position
    self.drone_position = Point()

    # Start the drone a little bit off the ground
    self.goal_cmd.z = 3.0

    # Keeps track of whether the goal  position was changed or not
    self.goal_changed = False

    # Call the mainloop of our class
    self.mainloop()

  # CHECKPOINT 5
  def toggleGeofence(self, request):
    if request.geofence_on == False:
      self.geofence_on = False
    else:
      self.geofence_on = True
    return toggle_geofenceResponse(True)


  # Callback for the keyboard manager
  def getKeyboardCommand(self, msg):
    # Save the keyboard command
    if self.state == DroneState.HOVERING:
      self.goal_changed = True
      self.goal_cmd = copy.deepcopy(msg)


  # TO BE COMPLETED FOR CHECKPOINT 2
  # TODO: Add function to receive drone's position messages
  def getDronePosition(self, msg):
    self.drone_position = msg.pose.position


  # Converts a position to string for printing
  def goalToString(self, msg):
    pos_str = "(" + str(msg.x) 
    pos_str += ", " + str(msg.y)
    pos_str += ", " + str(msg.z) + ")"
    return pos_str


  # TO COMPLETE FOR CHECKPOINT 4
  # TODO: Implement processVerifying
  def processVerifying(self):
    # Check if the new goal is inside the geofence
    # If it is change state to moving
    # If it is not change to hovering
    rospy.loginfo(str(rospy.get_name()) + ": Current State: VERIFYING")
    if ((self.geofence_x[0] <= self.goal_cmd.x <= self.geofence_x[1]) and (self.geofence_y[0] <= self.goal_cmd.y <= self.geofence_y[1]) and (self.geofence_z[0] <= self.goal_cmd.z <= self.geofence_z[1])) or self.geofence_on == False:
      self.state = DroneState.MOVING
      rospy.loginfo(str(rospy.get_name()) + ": Current State: MOVING")
    else:
      self.state = DroneState.HOVERING
      rospy.loginfo(str(rospy.get_name()) + ": Current State: HOVERING")
    pass


  # This function is called when we are in the hovering state
  def processHovering(self):
    # Print the requested goal if the position changed
    if self.goal_changed:
      rospy.loginfo(str(rospy.get_name()) + ": Requested Position: " + self.goalToString(self.goal_cmd))
      # TO BE COMPLETED FOR CHECKPOINT 4
      # TODO: Update
      self.processVerifying()
      self.goal_changed = False


  # This function is called when we are in the moving state
  def processMoving(self):
    # Compute the distance between requested position and current position
    dx = self.goal_cmd.x - self.drone_position.x
    dy = self.goal_cmd.y - self.drone_position.y
    dz = self.goal_cmd.z - self.drone_position.z

    # Euclidean distance
    distance_to_goal = sqrt(pow(dx, 2) + pow(dy, 2) + pow(dz, 2))
    # If goal is reached transition to hovering
    if distance_to_goal < self.acceptance_range:
      self.state = DroneState.HOVERING
      rospy.loginfo(str(rospy.get_name()) + ": Complete")
      rospy.loginfo(str(rospy.get_name()) + ": ----------------------------------")
      rospy.loginfo(str(rospy.get_name()) + ": Current State: HOVERING")


  # The main loop of the function
  def mainloop(self):
    # Set the rate of this loop
    rate = rospy.Rate(20)

    # While ROS is still running
    while not rospy.is_shutdown():
      # Publish the position
      self.position_pub.publish(self.goal_cmd)

      # Check if the drone is in a moving state
      if self.state == DroneState.MOVING:
        self.processMoving()
      # If we are hovering then accept keyboard commands
      elif self.state == DroneState.HOVERING:
        self.processHovering()
      elif self.state == DroneState.VERIFYING:
        self.processVerifying()

      # Sleep for the remainder of the loop
      rate.sleep()


if __name__ == '__main__':
  rospy.init_node('geofence_mission_node')
  try:
    ktp = GeofenceAndMission()
  except rospy.ROSInterruptException:
    pass
