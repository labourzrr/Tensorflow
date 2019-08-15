import numpy as np
import cv2

img = cv2.imread("lena.jpg")
img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
hsv = img_hsv.copy()
hsv[:,:,0] = (hsv[:,:,0] - 30)%180
hsv_img = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
cv2.imshow("img",hsv_img)
cv2.waitKey(0)
