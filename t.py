import numpy as np
import cv2 as cv
cap = cv.VideoCapture('./lightvedio.MP4')
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # 逐帧捕获
    ret, frame = cap.read()
    # 如果正确读取帧，ret为True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # 具体框架
    # 尺寸
    frame = cv.resize(frame,(1080, 1920))

    imgray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #图像阈值处理
    ret, thresh = cv.threshold(imgray, 150, 255, cv.THRESH_BINARY)

    #进行侵蚀或者扩张
    kernel = np.ones((3,3),np.uint8) #用numpy创建数组
    erosion = cv.erode(thresh,kernel,iterations = 1)
    dilation = cv.dilate(erosion,kernel,iterations = 2) # 进行扩张


    # 轮廓检测
    contours, hierarchy = cv.findContours(dilation, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    # 绘制轮廓
    #cv.drawContours(im, contours, -1, (0,23,255), 2)

    # 筛选
    # 1.边界矩形
    maxarea=0
    for cnt in contours:
        #area = cv.contourArea(cnt)

        # 旋转矩形
        rect = cv.minAreaRect(cnt)
        ocenter=rect[0]
        box = cv.boxPoints(rect)
        box = np.int0(box)
        area = cv.contourArea(box)
        if area>maxarea and area >16000:
            maxarea=area
        #cv.drawContours(frame, cnt, -1, (0,0,255), 5)
    nearea=1000000
    for cnt in contours:
        rect = cv.minAreaRect(cnt)
        ocenter=rect[0]
        box = cv.boxPoints(rect)
        box = np.int0(box)
        area = cv.contourArea(box)
        if area >= maxarea :
            # cv.drawContours(frame,[box],0,(0,0,255),4)
            # 记录该矩形的范围(获取四个顶点坐标)
            # left_point_x = np.min(box[:, 0])
            # right_point_x = np.max(box[:, 0])
            # top_point_y = np.min(box[:, 1])
            # bottom_point_y = np.max(box[:, 1])
            ocenter=rect[0]

            for cnt2 in contours:
                center,rag,angle = cv.minAreaRect(cnt2)
                rect2 = cv.minAreaRect(cnt2)
                box2 = cv.boxPoints(rect2)
                box2 = np.int0(box2)
                area2 = cv.contourArea(box2)

                if abs(center[0]-ocenter[0])<80 and abs(center[1]-ocenter[1])<80:
                    if area2<nearea and area2>12 :
                        nearea=area2
                        necnt = cnt2
                    #print(area2)
                    cv.drawContours(frame, cnt2, -1, (0,233,0), 2)

            break
    #print(necnt)
    cv.drawContours(frame,necnt,-1,(0,0,255),10)
    frame = cv.resize(frame,(1000,500))
    cv.imshow('11',frame)


    cv.waitKey(0)
    # if cv.waitKey(1) == ord('q'):
    #     break
# 完成所有操作后，释放捕获器
cap.release()
cv.destroyAllWindows()