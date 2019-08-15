import numpy as np
import cv2

img = cv2.imread("lena.jpg")
M_copy_img = np.array([[0,0.8,100],
                       [0.5,0,50]],dtype = np.float32)
img_changed = cv2.warpAffine(img,M_copy_img,(500,500))
cv2.imshow("img",img_changed)
cv2.waitKey(0)