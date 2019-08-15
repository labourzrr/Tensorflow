import numpy as np
import cv2
import random

img = np.mat(np.zeros((600,600),dtype = np.uint8))

imgByteArray = bytearray(img)
print(imgByteArray)

imgBGR = np.array(imgByteArray).reshape(600,600)

cv2.imshow("cool",imgBGR)
cv2.waitKey(0)