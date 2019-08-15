import numpy as np
import cv2
from scipy import ndimage
kerne133 = np. array([[-1,-1,-1],
                      [-1,8,-1],
                      [-1,-1,-1]])

kerne133_D = np.array([[1,1,1],
                       [1,-8,1],
                       [1,1,1]])

img = cv2.imread("lena.jpg",0)
lightImg = ndimage.convolve(img,kerne133)
cv2.imshow("img",lightImg)
cv2.waitKey(0)