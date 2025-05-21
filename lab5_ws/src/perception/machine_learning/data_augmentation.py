import os
import glob
import cv2
import numpy as np
import random

class DataAugmentation():

    # Input image, output a list of zoomed images
    # TODO: ONE OF THE OPTIONAL AUGMENTATIONS
    def zoom(self, img):
        # Create a list to hold the output
        output = []

        # Define the zoom percentages
        zoom_in = 2
        zoom_out = 1

        # For each zoom percentage
        # Get the image shape
        x, y, z = img.shape

        # Compute the new shape based on the zoom
        image_in = cv2.resize(img, None, fx= zoom_in, fy= zoom_in, interpolation= cv2.INTER_LINEAR)
        image_out = cv2.resize(img, None, fx= zoom_out, fy= zoom_out, interpolation= cv2.INTER_LINEAR)

        # Make the image the new shape
    
        # Pad or crop the image depending on original size
        x2, y2, z2 = image_in.shape
        x_bound = (x2 - x) / 2
        y_bound = (y2 - y) / 2
        
        image_in = image_in[x_bound:x2-x_bound, y_bound:y2-y_bound]
        image_out = cv2.copyMakeBorder(image_out, y_bound, y_bound, x_bound, x_bound, cv2.BORDER_CONSTANT, None, [0,0,0])
        
        # Save new image to list
        output.append(image_in)
        output.append(image_out)

        # Return list
        return output

    # Input image, output a list of translated images
    # TODO: ONE OF THE OPTIONAL AUGMENTATIONS
    def translate_image(self, img):
        # Create a list to hold the output
        # Define the translations
        # For each translation in X
            # For each translation in Y
                # Get the current image shape
                # Compute the new shape of the image
                # Warp the image to the new shape
                # Append black pixels to the edge
                # Save the new image
        # Return the output
        return None

    # Input image, output a list of rotated images
    # TODO: ONE OF THE OPTIONAL AUGMENTATIONS
    def rotate_image(self, img):
        # Create a list to hold the output
        # Define the rotation we want to consider
        # For each rotation
            # Get the image shape
            # Compute the rotation matrix centered around the middle of the image HINT: cv2.getRotationMatrix2D() 
            # Warp the image using the rotation matrix
            # Append the image to the output list
        # Return the output
        return None

    # Input image, output a list of blurred images
    # TODO: REQUIRED
    def blur_image(self, img):
        # Create a list to hold the output
        output = []

        # Define the blur amounts
        slight_blur = (5,5)
        signif_blur = (10,10)

        # For each blur amount
        # Blur the image HINT: cv2.blur
        # Append the image to the output list
        output.append(cv2.blur(img, slight_blur))
        output.append(cv2.blur(img, signif_blur))

        # Return the output
        return output

    # Input image, output a list of images with different brightness
    # TODO: REQUIRED
    def change_brightness(self, img):
        # Create a list to hold the output
        output = []

        # Define the brightness levels
        brighter = 50
        darker = 50

        # For each brightness level
        # Convert the image into HSV
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        
        # Add the brightness level to the V component
        h, s, v = cv2.split(hsv)
        lim = 255 - brighter
        v[v > lim] = 255
        v[v <= lim] += brighter

        h2, s2, v2 = cv2.split(hsv)
        lim2 = 0 + darker
        v2[v2 < lim2] = 0
        v2[v2 >= lim2] -= darker

        hsv_bright = cv2.merge((h, s, v))
        hsv_dark = cv2.merge((h2, s2, v2))
        
        # Revert to BRG format
        image_bright = cv2.cvtColor(hsv_bright, cv2.COLOR_HSV2BGR)
        image_dark = cv2.cvtColor(hsv_dark, cv2.COLOR_HSV2BGR)

        # Append the image to the output list
        output.append(image_bright)
        output.append(image_dark)

        # Return the output
        return output

    # Input image, output a list of noisy images
    # TODO: REQUIRED
    def add_noise(self, img):
        # Create a list to hold the output
        output = []

        # Define the mean and sigma values
        mean = 50
        sigma = 10

        # For each mean value
        # For each sigma value
        # Create random noise with the same shape as the image HINT: np.random.normal
        gauss = np.random.normal(mean, sigma, img.shape)

        # Add the noise to the image
        noisy_image = img + gauss

        # Save the new image to the output list
        output.append(noisy_image)

        # Return the output
        return output

    # Input image, output a list of images with a combination of the above functions
    # TODO: REQUIRED
    def combine_data_augmentation_functions(self, img):
        # Combine the above functions to return different combintations of transformations
        output = []

        zoom_images = self.zoom(img)
        blur_1 = self.blur_image(zoom_images[0])
        blur_2 = self.blur_image(zoom_images[1])
        
        output.append(blur_1[0])
        output.append(blur_1[1])
        output.append(blur_2[0])
        output.append(blur_2[1])

        return output
