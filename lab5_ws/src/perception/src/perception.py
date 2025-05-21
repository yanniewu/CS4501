#!/usr/bin/env python
import os
import cv2
import rospy
import pickle
import rospkg

import numpy as np

from cv_bridge import CvBridge

from std_msgs.msg import Bool
from std_msgs.msg import String
from sensor_msgs.msg import Image

from sklearn.neural_network import MLPClassifier
from marine_life_detection import MarineLifeDetection

# Create a class which we will use to take keyboard commands and convert them to a position
class Perception():
  # On node initialization
  def __init__(self):
    # Allows us to read images from rostopics
    self.bridge = CvBridge()

    # Marine Life Detection node
    self.detector = MarineLifeDetection()
    self.detected = False
    self.classification = None
    self.image = None

    # Load the classes
    self.classes = ['dolphin', 'seal', 'penguin']

    # # Load the model
    rp = rospkg.RosPack()
    model_path = os.path.join(rp.get_path("perception"), "machine_learning", "model.pkl")
    self.model = None
    if os.path.exists(model_path):
      with open(model_path, 'rb') as f:
        self.model = pickle.load(f)

    # TODO Checkpoints 3 & 4
    # Create the publishers and subscriber
    self.image_sub = rospy.Subscriber("/uav/sensors/camera", Image, self.downfacing_camera_callback)
    self.marine_life_pub = rospy.Publisher("/marine_life_detected", Bool, queue_size=1)
    self.marine_class_pub = rospy.Publisher("/marine_life_classification", String, queue_size=1)

    # Call the mainloop of our class
    self.mainloop()

  def downfacing_camera_callback(self, msg):
    # TODO Checkpoint 3
    # Convert to opencv format using self.bridge
    cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='passthrough')

    # Use functions implemented in `marine_life_detection.py` to determine if animal is present
    # Save to self.detected
    mask = self.detector.create_marine_life_mask(cv_image)
    segmented_image = self.detector.segment_image(cv_image, mask) 
    gray = cv2.cvtColor(segmented_image, cv2.COLOR_BGR2GRAY)
    self.detected = self.detector.marine_life_detected(gray)

    # TODO Checkpoint 4
    # Save the opencv image to self.image so it can be processed further in the mainloop
    self.image = cv_image
    
  # Can be used to get image into the right structure to be passed into the model for CHECKPOINT 4
  # This function replaces `load_image` in the `classify_single_image` example
  def preprocess_image(self, img):
    # Reshape and convert to gray
    img = cv2.resize(img, (48, 48))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    x = img.reshape((1, -1))
    x = x.astype('float32')
    x = x / 255.0
    return x

  def mainloop(self):
    # Set the rate of this loop
    rate = rospy.Rate(0.25)

    classes = ['dolphin', 'seal', 'penguin']

    # While ROS is still running
    while not rospy.is_shutdown():

      # TODO Checkpoint 3
      # Publish wether an animal was detected on /marine_life_detected
      self.marine_life_pub.publish(self.detected)

      ####################################
      # Comment this out if you are on M1
      ####################################
      if self.model is not None:
        if self.detected:
        # TODO Checkpoint 4
        # If the animal was detected
        # Load the image (using self.preprocess_image)
          processed_image = self.preprocess_image(self.image)
          # Predict what class it is
          prediction = self.model.predict(processed_image)
          # Get the class index using argmax
          result = np.argmax(prediction, axis=-1)
          # Save the classification to self.classification
          self.classification = str(classes[result[0]])

        if self.classification is not None:
          # TODO CHeckpoint 4
          # Publish the class on /marine_life_classification
          self.marine_class_pub.publish(self.classification)

      ####################################

      # Sleep for the remainder of the loop
      rate.sleep()


if __name__ == '__main__':
  rospy.init_node('PerceptionNode')
  try:
    ktp = Perception()
  except rospy.ROSInterruptException:
    pass