import numpy as np
import cv2
img = np.zeros((600,600))

img[0,0] = 255

cv2.imshow("test",img)
cv2.waitKey(0)