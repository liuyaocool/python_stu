import cv2
import matplotlib.pyplot as plt
import numpy as np

# 显示图片方法
def showimg(img):
	plt.imshow(img)
	plt.axis('off') # 坐标轴
	plt.show()
# 读取图片
def imgread(imgurl):
	img = cv2.imread(imgurl)
	# 因颜色通道不一样 需要转换
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	return img

def colorrand():
	return np.random.randint(0, 255,size=(3,)).tolist()