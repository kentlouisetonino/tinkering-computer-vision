import cv2
import sys

# Read the image.
# If you print the img, it return a matrix of pixels with values from 0 to 255.
img = cv2.imread(cv2.samples.findFile("images/drone.jpg"))

# Check if the file exist.
if img is None:
    sys.exit("Could not read the image.")

# Display the image.
cv2.imshow("Drone Image", img)

# Wait for the user to enter a key.
cv2.waitKey(0)
