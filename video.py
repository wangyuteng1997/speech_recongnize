# -*- coding: utf-8 -*-
# @Time    : 2021/1/4 9:33
# @Author  : WANG Yuteng
# @FileName: video.py

import numpy as np
import cv2

def camera():
    font = cv2.FONT_HERSHEY_SIMPLEX
    lower_green = np.array([35, 110, 106])
    upper_green = np.array([77, 255, 255])
    lower_red = np.array([0, 127, 128])
    upper_red = np.array([10, 255, 255])
    lower_blue = np.array([100, 43, 46])
    upper_blue = np.array([124, 255, 255])

    # cap = cv2.VideoCapture('1.mp4')
    cap = cv2.VideoCapture(0)
    if (cap.isOpened()):
        flag = 1
    else:
        flag = 0

    if (flag):
        num_red = 0
        num_green = 0
        num_blue = 0
        ret, frame = cap.read()  # 读取一帧

        hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask_green = cv2.inRange(hsv_img, lower_green, upper_green)  # 根据颜色范围删选
        mask_red = cv2.inRange(hsv_img, lower_red, upper_red)
        mask_blue = cv2.inRange(hsv_img, lower_blue, upper_blue)
        # 根据颜色范围删选
        mask_green = cv2.medianBlur(mask_green, 7)  # 中值滤波
        mask_red = cv2.medianBlur(mask_red, 7)  # 中值滤波
        mask_blue = cv2.medianBlur(mask_blue, 7)

        contours, hierarchy = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        contours2, hierarchy2 = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        contours3, hierarchy3 = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        for cnt in contours:
            (x, y, w, h) = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
            cv2.putText(frame, "Green", (x, y - 5), font, 0.7, (0, 255, 0), 2)
            num_green = num_green + 1

        for cnt2 in contours2:
            (x2, y2, w2, h2) = cv2.boundingRect(cnt2)
            cv2.rectangle(frame, (x2, y2), (x2 + w2, y2 + h2), (0, 255, 255), 2)
            cv2.putText(frame, "Red", (x2, y2 - 5), font, 0.7, (0, 0, 255), 2)
            num_red = num_red + 1

        for cnt3 in contours3:
            (x3, y3, w3, h3) = cv2.boundingRect(cnt3)
            cv2.rectangle(frame, (x3, y3), (x3 + w3, y3 + h3), (0, 255, 255), 2)
            cv2.putText(frame, "blue", (x3, y3 - 5), font, 0.7, (0, 0, 255), 2)
            num_blue = num_blue + 1

    #cv2.imshow("dection", frame)
    #cv2.imwrite("imgs/%d.jpg" % num, frame)
    print("------------------------------")
    print("in the camera :")
    print("there is red objects", num_red)
    print("there is green objects", num_green)
    print("there is blue objects", num_blue)
    print("------------------------------")
    #cv2.waitKey(0)
    #cv2.d
    return num_green,num_red,num_blue



