
#可实现点击图像读出该点的HSV值

import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
# Example：
image = cv2.imread('train_dataset/hwd2.jpg')
#img = Image.open('hwd1.jpg')
HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# hlist = [0 for i in range(256)]
# slist = [0 for i in range(256)]
# vlist = [0 for i in range(256)]


def getpos(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN: #定义一个鼠标左键按下去的事件
        #print(HSV[y,x])
        print(HSV[y,x])
        #print(RGB[y,x])

if __name__ == "__main__":
#     PlotBarTest1()
    #image = cv2.resize(image, (1024,768))
    #HSV = cv2.resize(HSV, (1024,768))
    #cv2.namedWindow('imageHSV',cv2.WINDOW_NORMAL)
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    #cv2.imshow("imageHSV",HSV)
    cv2.imshow('image', image)
    cv2.setMouseCallback("image", getpos)
    cv2.waitKey(0)

