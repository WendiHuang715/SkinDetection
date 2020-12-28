# SkinDetection
Skin color detection based on Bayesian estimation

长理模式识别课堂作业
对图像H值进行贝叶斯判别实现的肤色检测

  ## 仅供交流学习
## 切勿直接复制粘贴

实验前先下载好项目中所需要用到的包，例如Python，numpy, PIL, cv2等
安装Python后，在cmd输入指令：
# 下载安装numpy指令
pip install numpy  
# 下载安装PIL指令
pip install pillow
# 下载cv2
pip install opencv-python
复现属于自己的作业：


## 1.拍一张手的照片，放入train_dataset文件夹中
此项目中照片尺寸皆为3648 * 2736，其他尺寸的照片需要修改一下代码：

以 2736 * 2736 的照片为例（凡是涉及到打点、读点的循环都要按这个修改）
for i in range(18):# 每行打18个点，你可以把18改成一个能被2736整除的数
     for j in range(18): # 每列打18个点，你可以把18改成一个能被2736整除的数
          cv2.circle(img, (152 * j - 1, 152 * i - 1), 25, (200, 100, 100), 3) # 2736/18 = 152

## 2.打开point_dot.py, 根据你所上传的照片文件名修改代码，运行代码

以上传照片名为abc.jpg为例，需要修改这几行：
img = cv2.imread('abc.jpg')
cv2.imwrite('pic5.jpg', img) # 不要跟point_set中已有的照片名字重复就行，这里取名pic5.jpg

另：
for i in range(18):
     for j in range(24):
         if [i, j] in skinlist[4]:
             cv2.circle(img, (152 * j - 1, 152 * i - 1), 25, (200, 100, 100), 3)
         else:
             cv2.circle(img, (152 * j - 1, 152 * i - 1), 25, (100, 200, 100), 3)
需改成：
for i in range(18):
     for j in range(24):
          cv2.circle(img, (152 * j - 1, 152 * i - 1), 25, (100, 200, 100), 3)

## 3.打标签：
打开打点以后的照片（即本例中的pic5.jpg）,打开skinlabel.py,新建一个list(在本例中取名skinlist5)
仔细看打点后的照片，凡是绿圆的中心点落在皮肤上的，都要记录到skinlist5中
（如 第一行第三列的点落在皮肤上，在skinlist中添加元素 [0, 2] ,注意不是 [1, 3]）
以此类推，慢慢数点，得到完整的skinlist5，在最底下的skinlist中添加skinlist5
由：
skinlist = [skinlist1, skinlist2, skinlist3, skinlist4]
变成：
skinlist = [skinlist1, skinlist2, skinlist3, skinlist4, skinlist5]

## 4.重新打开point_dot.py， 把循环改回来。
由：
for i in range(18):
     for j in range(24):
          cv2.circle(img, (152 * j - 1, 152 * i - 1), 25, (100, 200, 100), 3)
          
改成：
for i in range(18):
     for j in range(24):
         if [i, j] in skinlist[4]: # skinlist[4] 就是 skinlist5
             cv2.circle(img, (152 * j - 1, 152 * i - 1), 25, (200, 100, 100), 3)
         else:
             cv2.circle(img, (152 * j - 1, 152 * i - 1), 25, (100, 200, 100), 3)
             
## 5.以上操作都确保正确，在main.py中把最底下main函数中：
test('./hwd1.jpg', hp_c_s, hp_c)
改成
test('./abc.jpg', hp_c_s, hp_c) 
运行main.py，在test_output中找到自己的输出图片

## (选做)6.运行Analysis，可得到各个h值的统计图。统计图可以放入到论文中，作为分析材料。



