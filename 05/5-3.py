import numpy as np
import cv2
import os

randomByteArray = bytearray(os.urandom(120000))

flatByteArray = np.array(randomByteArray).reshape(300,400)
cv2.imshow("cool",flatByteArray)
cv2.waitKey(0)