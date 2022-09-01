import cv2
import os
import numpy as np
import math

class LineDetector():
    def __init__(self, scale_factor):
        self.images_count = 0 # for showing images purposes

        img = cv2.imread(os.path.join('imgs', '0000000.tiff'), cv2.IMREAD_GRAYSCALE)

        print(f'Original Dimensions: {img.shape}')
        print(f"Downscale factor {scale_factor}")
        self.width = int(img.shape[1] / scale_factor)
        self.height = int(img.shape[0] / scale_factor)
        dim = (self.width, self.height)
        
        # resize image
        img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        print(f'Resized Dimensions: {img.shape}')
        self.show("Original", img)

        # Ranged
        lower = np.array([230])
        upper = np.array([255])
        img = cv2.inRange(img, lower, upper)
        self.show("Ranged", img)

        # Canny
        img = cv2.Canny(img, 200, 400)
        self.show("Canny", img)

        line_segments = self.detect_line_segments(img)

        new_img = np.zeros_like(img)
        # Show lines
        self.show_line_segments(line_segments, new_img)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def show(self, img_name, img):
        columns = 3
        cv2.imshow(img_name, img)
        # TODO if img_name not exist:
        cv2.moveWindow(img_name,
                       self.width * math.floor(self.images_count % columns),
                       self.height * math.floor(self.images_count / columns))
        self.images_count +=1

    def detect_line_segments(self, img):
        # tuning min_threshold, minLineLength, maxLineGap is a trial and error process by hand
        rho = 1  # distance precision in pixel, i.e. 1 pixel
        angle = np.pi / 180  # angular precision in radian, i.e. 1 degree
        min_threshold = 10  # minimal of votes
        line_segments = cv2.HoughLinesP(img, rho, angle, min_threshold, 
                                        np.array([]), minLineLength=8, maxLineGap=4)

        return line_segments

    def show_line_segments(self, line_segments, this_img):
        for line in line_segments:
            print(f"Line: {(line[0][0], line[0][1])} ,{(line[0][2], line[0][3])}")    
            cv2.line(this_img, (line[0][0],line[0][1]), (line[0][2], line[0][3]), (150),2)
        self.show("Lines", this_img)

line_detector = LineDetector(scale_factor = 4)