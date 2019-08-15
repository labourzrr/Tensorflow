import cv2
img = cv2.imread("lena.jpg")
rows,cols,depth = img.shape
img_change = cv2.getRotationMatrix2D((rows/2,cols/2),45,0.6)
res = cv2.warpAffine(img,img_change,(500,500))
cv2.imshow("img",res)
cv2.waitKey(0)