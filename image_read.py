import cv2
import os

img = cv2.imread(os.path.join('imgs', '0000000.tiff'))

# display
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()