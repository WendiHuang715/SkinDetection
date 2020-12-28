#可识别
import numpy as np
import cv2
from PIL import Image
from skinlabel import skinlist, num_skinlabel
import os
import time

#train_set_path = './train_dataset/'

def trainset_Loader():
    #files = os.listdir(r'D:\project\SkinColorDetection\train_dataset')
    files = os.listdir(r'./train_dataset')
    num_jpg = len(files)
    hlist = [0 for x in range(180)]
    chlist = [0 for y in range(180)]
    hp_c_s = [0 for z in range(180)]  # 已知是皮肤的前提下，该点的h值为某值的概率列表
    hp_c = [0 for w in range(180)]  # 整张图片里面某h值的概率列表
    os.chdir(r'./train_dataset')
    for i in range(num_jpg):
        #image = cv2.imread(path + "hwd{}.jpg".format(i))
        image = cv2.imread(files[i])
        HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        for j in range(18):
            for k in range(24):
                if [j, k] in skinlist[i]:
                    hlist[HSV[j * 152 - 1, 152 * k - 1][0]] += 1
                chlist[HSV[j * 152 - 1, 152 * k - 1][0]] += 1
    for l in range(180):
        hp_c_s[l] = hlist[l] / num_skinlabel
        hp_c[l] = chlist[l] / (432 * num_jpg)
    return hlist, chlist, hp_c_s, hp_c

# #贝叶斯统计法
def test(test_image_path,hp_c_s, hp_c, R=0.5):
    image = cv2.imread(test_image_path)
    img = Image.open(test_image_path)
    width = img.size[0]#长度
    height = img.size[1]#宽度
    HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    for i in range(0, width):#遍历所有长度的点
        for j in range(0, height):#遍历所有宽度的点
            if hp_c[HSV[j, i][0]] == 0:
                img.putpixel((i, j), (255, 255, 255, 255))
            elif hp_c_s[HSV[j, i][0]] * 0.3279 / hp_c[HSV[j, i][0]] >= R:
                pass
            else:
                img.putpixel((i, j), (255, 255, 255, 255))
    img = img.convert("RGB")#把图片强制转成RGB
    t = time.localtime()
    localtime = '{}-{}-{}-{}'.format(t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min)
    print(os.getcwd())
    os.chdir(r'../test_output')
    img.save('{}.jpg'.format(localtime))

#保存修改像素点后的图片

if __name__ == '__main__':
    hlist, chlist, hp_c_s, hp_c = trainset_Loader()
    test('./hwd1.jpg', hp_c_s, hp_c)
    os.chdir(r'../all_data')
    np.savetxt("hlist.txt",hlist)
    np.savetxt("chlist.txt", chlist)
    np.savetxt("hp_c.txt", hp_c)
    np.savetxt("hp_c_s.txt", hp_c_s)
