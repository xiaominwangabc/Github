import numpy as np
import cv2 as cv
cv.namedWindow('image',cv.WINDOW_NORMAL)
img = cv.imread('sample.jpg',0)
cv.imshow('image',img)
k = cv.waitKey(0) & 0xFF
if k == 27:         # 等待ESC退出
    cv.destroyAllWindows()
elif k == ord('s'): # 等待关键字，保存和退出
    cv.imwrite('sample.jpg',img)
    cv.destroyAllWindows()