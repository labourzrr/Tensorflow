import numpy as np
import cv2
import random

img = np.random.randint(0,256,(600,600),dtype = np.uint8)
img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
print(img.shape)
cv2.imshow("test",img)
cv2.waitKey(0)

img1 = np.mat(np.zeros((300,300),dtype = np.uint8))
cv2.imshow("test",img1)
cv2.waitKey(0)

image = cv2.imread("jpg1.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imwrite("png3.png",image)
cv2.imshow("test",image)
cv2.waitKey(0)
