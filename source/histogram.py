import cv2
import numpy as np
from matplotlib import pyplot as plt
img =cv2.imread("gray.jpg")
img_gr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("figure1",img_gr)

hist,bins = np.histogram(img_gr.flatten(),256,[0,256])
h, w = img.shape[:2]
s = h*w
k = 0
q = 0.05
n = s*q
indB = 0
for i,v in enumerate(hist):
    k+=v
    if(k>=n):
        indB=i
        break
k = 0
indW = 0
for i, v in enumerate(reversed(hist)):
    k+=v
    if(k>=n):
        indW=i
        break
indW = len(hist)-indW
print(indB,indW)
plt.figure(1)
plt.plot(hist)
plt.show(block=False)

def fun(x):
    if x < indB:
        return 0
    if x >= indW:
        return 255
    return (x - indW) * 255 / (indW - indB) + 255

final = img_gr.copy()
for i in range(img_gr.shape[0]):
    for j in range(img_gr.shape[1]):
        final[i,j] = fun(img_gr[i,j])

hist = cv2.calcHist([final],[0],None,[256],[0,256])
cv2.imshow("figure2",final)
plt.figure(2)
plt.plot(hist)
plt.show()

