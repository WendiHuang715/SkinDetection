#打点

from PIL import Image
from pylab import imshow
from pylab import array
from pylab import plot
from pylab import title
import cv2
from skinlabel import skinlist
# 读取图像到数组中
import os
os.chdir('./train_dataset')
img = cv2.imread('hwd2.jpg')
for i in range(18):
     for j in range(24):
         if [i, j] in skinlist[1]:
             cv2.circle(img, (152 * j - 1, 152 * i - 1), 25, (200, 100, 100), 3)
         else:
             cv2.circle(img, (152 * j - 1, 152 * i - 1), 25, (100, 200, 100), 3)

cv2.imshow('image', img)
os.chdir('../point_set')
cv2.imwrite('pic2.jpg', img) #保存图片而且可以用于转换格式
cv2.waitKey(0)               #等待按键反应
cv2.destroyAllWindows()

