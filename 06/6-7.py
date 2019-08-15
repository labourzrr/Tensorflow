import numpy as np
import cv2
import random
img = cv2.imread("lena.jpg")
img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
hsv = img_hsv.copy()

hsv[:,:,0] = (hsv[:,:,0] + np.random.randint(50)) % 180
hsv[:,:,1] = (hsv[:,:,1] + np.random.randint(100)) % 180
hsv[:,:,2] = (hsv[:,:,2] + np.random.randint(50)) % 180
hsv_img = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)

gamma_change = [np.power(x/255,0.4) * 255 for x in range(256)]
gamma_img = np.round(np.array(gamma_change)).astype(np.uint8)
img_corrected = cv2.LUT(hsv_img,gamma_img)
cv2.imshow("img",img_corrected)
cv2.waitKey(0)
