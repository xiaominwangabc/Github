import numpy as np
import cv2 as cv

# cv.imread(图像路径，读取图像的方式)
# 读取图像的方式：
# cv.IMREAD_COLOR：-- 1 加载彩色图像。任何图像的透明度都会被忽视。它是默认标志。
# cv.IMREAD_GRAYSCALE：-- 0 以灰度模式加载图像
# cv.IMREAD_UNCHANGED：-- -1 加载图像，包括alpha通道
im = cv.imread('sample.jpg')

#
im = cv.resize(im,(500,400))
#
im = im[7:220,149:328]
#
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
#
ret, thresh = cv.threshold(imgray, 180, 255, cv.THRESH_BINARY)
#
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
newcontours=[]
cv.drawContours(im, contours, -1, (24,232,20), 2)
for item in contours:
    area = cv.contourArea(item)
    print(area)
    if area >2400 and area <2800:
        newcontours.append(item)
    


contours0, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
dst1=cv.drawContours(im,contours0, -1, (244,25,255), 2)
cv.imshow('Display',im)
cv.waitKey()
