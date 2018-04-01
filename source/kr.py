import numpy as np;
import cv2 as cv;
import matplotlib.pyplot as plt;
import math
colors=[(0,0,0),(127,127,127),(255,255,255)]
figures=[0,1,2]
power=5
def get_colors(i):
    if (i==0):
        return [0,1]
    if (i==1):
        return [0,2]
    if (i==2):
        return [1,2]
    if (i==3):
        return [1,0]
    if (i==4):
        return [2,0]
    if (i==5):
        return [2,1]
def create_figure(img,x,y):
    figure_num = np.random.randint(low=0,high=2)
    if (figure_num==0):
        draw_square(img,x,y);
    if (figure_num==0):
        a=1
        #draw_triang(img,x,y);
    if (figure_num==2):
        a=2
        #draw_circle(img,x,y);
def draw_square(img,x,y,color_):
    x2=int((x+10*power+x)/2)
    y2=int((y+10*power+y)/2)

    cv.rectangle(img,(x,y),(x+10*2*power,y+10*2*power),colors[color_[0]],-1)

    cv.rectangle(img,(x2,y2),(x2+10*power,y2+10*power),colors[color_[1]],-1)
def draw_circle(img,x,y,color_):
    cv.rectangle(img,(x,y),(x+10*2*power,y+10*2*power),colors[color_[0]],-1)
    center=((x+10*power),(y+10*power))
    cv.circle(img,center,5*power,colors[color_[1]],-1)
def draw_triang(img,x,y,color_):
    cv.rectangle(img, (x, y), (x + 10 * 2 * power, y + 10 * 2 * power), colors[color_[0]],-1)
    x2=x+power*6
    y2=y+power*6
    triang = np.array([[[x2, y2], [x2, y2+20], [x2+20, y2]]], dtype=np.int32)
    cv.fillPoly(img, triang, colors[color_[1]])
img = np.zeros((800,800),np.int16)
x=0
y=0
for i in range(6):
    y=y+10*2*power
    draw_triang(img,x,y,get_colors(i))
x=10*2*power
y=0
for i in range(6):
    y=y+10*2*power
    draw_circle(img,x,y,get_colors(i))
x=2*10*2*power
y=0
for i in range(6):
    y=y+10*2*power
    draw_square(img,x,y,get_colors(i))

cv.imshow("image",np.uint8(img))
kernel1 = np.array([[-1/9, -1/9, -1/9],[0,0,0],[1/9,1/9,1/9]])
map1 = cv.filter2D(img, -1, kernel1)

kernel2 = np.array([[-1/9, 0,1/9],[-3/9,0,3/9],[-1/9,0,1/9]])
map2 = cv.filter2D(img, -1, kernel2)

sobelx = cv.Sobel(img,cv.CV_64F,1,0,ksize=1)
sobely = cv.Sobel(img,cv.CV_64F,0,1,ksize=1)
#cv.imshow("Img",sobelx)
#cv.imshow("Img2",sobely)

arrimage1 = np.asarray(sobelx,np.int32)
arrimage2 = np.asarray(sobely,np.int32)

for i in range (arrimage1.__len__()):
    for j in range (arrimage1[i].__len__()):
        arrimage1[i,j]=arrimage1[i,j]/2+128
        arrimage2[i,j]=arrimage2[i,j]/2+128
arrim1=arrimage1.astype(np.uint8)
arrim2=arrimage2.astype(np.uint8)
cv.imshow("arrim",arrim1)
cv.imshow("arri2",arrim2)

newim = np.zeros((800,800),np.uint8)
finalimage= np.zeros((800,800,3),np.uint8)
for i in range (arrimage1.__len__()):
    for j in range (arrimage1[i].__len__()):
        tmp1 = np.int32(arrimage1[i,j])*np.int32(arrimage1[i,j])
        tmp2 = np.int32(arrimage2[i, j]) * np.int32(arrimage2[i, j])
        tmp3 = tmp1+tmp2
        tmp4 = math.sqrt(tmp3)
        #tmpval = int(math.sqrt(arrimage1[i,j]*arrimage1[i,j]+arrimage2[i,j]*arrimage2[i,j]))
        newim[i, j] = np.uint8(tmp4)
        finalimage[i,j,0]=newim[i,j]
        finalimage[i,j,1]=arrimage1[i,j]
        finalimage[i,j,2]=arrimage2[i,j]
cv.imshow("finalimg",finalimage.astype(np.uint8))
cv.imshow("newim",newim.astype(np.uint8))


cv.waitKey(0)