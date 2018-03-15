import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("d://gray.jpg")
canvas = np.zeros((100,100),dtype=np.uint8)
#canvas=cv2.circle(canvas,(50,50),20,(255,),-1)
arr1= np.array([[-1/2,1/2]])
filtered = cv2.filter2D(img,-1,kernel=arr1)
#hsvimg = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

plt.imshow(filtered)
plt.show()