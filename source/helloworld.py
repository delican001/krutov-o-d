import numpy as np
import cv2

#image = np.zeros((800,600))
image = cv2.imread('C:png.png')
fontFace = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1.0
thickness = 2
textOrg = (50, 50)
cv2.putText(image,'Hello World!', textOrg, fontFace, fontScale, 255, thickness, 9)
cv2.imshow('Hello World', image)
cv2.waitKey()