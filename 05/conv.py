import numpy as np
import cv2

def convolve(dataMat,kernel):
    m,n = dataMat.shape
    mk,nk = kernel.shape
    newMat = np.ones(((m - mk + 1),(n - nk + 1)))
    tempMat = np.ones(((mk),(nk)))
    for row in range(m - mk + 1):
        for col in range(n - nk + 1):
            for m_k in range(mk):
                for n_k in range(nk):
                    tempMat[m_k,n_k] = dataMat[(row + m_k),(col + n_k)] * kernel[m_k,n_k]
            newMat[row,col] = np.sum(tempMat)
    return newMat

img = cv2.imread("lena.jpg",0)
kernel = np.array([[-1,-1,-1],
                   [-1,8,-1],
                   [-1,-1,-1]])

lightImg = convolve(img,kernel)
cv2.imshow("img",lightImg)
cv2.waitKey(0)