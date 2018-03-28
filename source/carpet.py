import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = np.zeros((256,256,3),dtype=np.uint8)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        for k in range(img.shape[2]):
            img[i, j, 0] = 64 * np.sin(i / 16) + 128
            img[i, j, 1] = 64 * np.sin(j / 16) + 128
            img[i, j, 2] = 64 * np.sin(k / 16) + 128
cv.imshow("Img",img)
cv.waitKey(0)