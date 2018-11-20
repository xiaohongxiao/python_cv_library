# -*- coding:utf-8 -*-
import cv2
import numpy as np
import datetime
##########################################################################################
##视频路径 宏定义区域
# windowName = "Video Control";  # 播放窗口名称
# currentFrame = 1.0;  # 当前播放帧
# trackBarValue = 1;  # trackbar控制量
videos_path = 'rtsp://admin:qwe741852@192.168.20.64'



def read():
    # cv2.namedWindow(windowName)
    #cv2.createTrackbar(trackBarName, windowName, trackBarValue, trackBarMax, nothing)
    #trackbarFunc(0)
    # 遍历整个文件夹
    #files = os.listdir(root_path)
    #file = []
    capture = cv2.VideoCapture(videos_path)
    if not capture.isOpened():
        print("视频文件打开失败!")
    # frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))  # 取帧计数器 总帧数
    # frame_rate = int(capture.get(cv2.CAP_PROP_FPS))  # FPS 每秒传输帧数
    # print("视频的总帧数{} 视频的帧率{}", frame_count, frame_rate)
    # width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    # height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # print('视频尺寸（高，宽）：', height, width)

    loop_flag = 0
    pos = 0

    print(type(capture))
    while(True):
        a, cap = capture.read()
        print(cap)
        # cv2.imshow(windowName,cap)
        # 后续图像处理

    capture.release()


if __name__ == '__main__':
        read()

