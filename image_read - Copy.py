import cv2
import os
import numpy as np

img = cv2.imread(os.path.join('imgs', '0000000.tiff'), cv2.IMREAD_GRAYSCALE)

print(f'Original Dimensions: {img.shape}')
scale = 4
print(f"Downscale factor {scale}")
width = int(img.shape[1] / scale)
height = int(img.shape[0] / scale)
dim = (width, height)
 
# resize image
img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
print(f'Resized Dimensions: {img.shape}')

# display
cv2.imshow("Original", img)

lower = np.array([230])
upper = np.array([255])

img = cv2.inRange(img, lower, upper)

cv2.imshow("Ranged", img)
img= cv2.Canny(img, 200,400)
cv2.imshow("canny", img)

cv2.waitKey(0)
cv2.destroyAllWindows()