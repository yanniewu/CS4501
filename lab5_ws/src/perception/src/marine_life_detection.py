#!/usr/bin/env python
import cv2
import numpy as np

# Create a class which we will use to take keyboard commands and convert them to a position
class MarineLifeDetection():
  
  def create_marine_life_mask(self, image):
    # Convert the image to the HSV format using opencv
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define your HSV upper values
    # Define your HSV lower values
    lower_bound = np.array([100,150,0],np.uint8)
    upper_bound = np.array([140,255,255],np.uint8)

    # Generate a mask using opencv inrange function.
    mask = cv2.inRange(hsv_image, lower_bound, upper_bound)

    # Return the mask
    return mask

  def segment_image(self, image, mask):
    # Return the bitwise_and of the image and the mask. Note opencv has a bitwise_and operation
    result = cv2.bitwise_and(image, image, mask=mask)

    # Return the resultant image
    return result

  def marine_life_detected(self, mask):
    # Compute the size of the mask
    total_pixels = mask.size

    # Compute the number of marine animal pixels in the mask
    animal_pixels = total_pixels - cv2.countNonZero(mask)

    # Use the ratio of these values to determine whether an animal was detected or not
    ratio = float(animal_pixels) / float(total_pixels)

    # Return whether an animal is detected or not
    if ratio >= 0.06:
      return True

    return False