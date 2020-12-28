import os
import numpy as np
from matplotlib import pyplot as plt


def Print_Analysis():
    files = os.listdir('./all_data')
    os.chdir('./all_data')
    a = {}
    for i in range(len(files)):
        a[i] = np.loadtxt(files[i])

    iIndex = {}
    ax = {}
    for i in range(len(files)):
        iIndex[i] = np.arange(len(a[i]))
        ax[i] = plt.subplot(2, 2, i+1)
        plt.sca(ax[i])
         # 绘制红色曲线
        plt.plot(iIndex[i], a[i])
        # 限制y坐标轴范围
        plt.xlim(0, len(np.loadtxt(files[i])))

    # 选择ax2
    plt.show()


if __name__ == '__main__':
    Print_Analysis()




