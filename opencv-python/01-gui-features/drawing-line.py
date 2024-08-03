import numpy
import cv2

# Create a black image.
image = numpy.zeros((500, 500, 3), numpy.uint8)

# Draw a diagonal blue line with thickness of 5 px.
cv2.line(image, (10, 10), (490, 490), (255, 0, 0), 2)

# Show the image.
cv2.imshow("Drawing Line", image);

# Wait for any key before exit.
cv2.waitKey(0)
