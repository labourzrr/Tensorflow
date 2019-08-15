import numpy as np
import cv2

img =  np.zeros((600,600))

img[:,300] = 255
img[200,:] = 255

cv2.imshow("img",img)
cv2.waitKey(0)