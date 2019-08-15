import numpy as np
import random
import cv2

img = cv2.imread("lena.jpg")
width,height,depth = img.shape
img_width_box  = width * 0.2
img_height_box = height * 0.2
for _ in range(9):
    start_pointX = int(random.uniform(0,img_width_box))
    start_pointY = int(random.uniform(0,img_height_box))
    copy_img = img[start_pointX:400,start_pointY:450]
    cv2.imshow("img",copy_img)
    cv2.waitKey(0)