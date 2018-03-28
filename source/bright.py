import numpy as np
import cv2 as cv

img = cv.imread("png.png")
imgcv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("Source",img)
cv.imshow("Source2BGR",imgcv)
#cv.waitKey(0)

p=60
img1=imgcv[:,:,2]
msk = img1<p
msk1=np.empty(msk.shape,dtype="uint8")
for i in range(msk.shape[0]):
    for j in range(msk.shape[1]):
        if msk[i,j]==True:
            msk1[i,j]=int(1)
        else:
            msk1[i,j]=int(0)
res=cv.bitwise_and(img,img,mask=msk1)
newimg=cv.threshold(img,p,255,cv.THRESH_BINARY)
cv.imshow("NewImg",res)
cv.waitKey(0)