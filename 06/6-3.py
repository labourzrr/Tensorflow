import numpy as np
import cv2
import matplotlib.pyplot as plt
img = plt.imread("lena.jpg")
gamma_change  = [np.power(x/255,0.2) * 255 for x in range(256)]
gamma_img = np.round(np.array(gamma_change)).astype(np.uint8)
img_correct = cv2.LUT(img,gamma_img)
plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(img_correct)
plt.show()