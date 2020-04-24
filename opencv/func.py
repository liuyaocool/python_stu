import cv2
import matplotlib.pyplot as plt
import numpy as np

# 显示图片方法
def showimg(img):
	plt.imshow(img)
	plt.axis('off') # 坐标轴
	plt.show()
# 显示图片方法
def showgray(img):
	plt.imshow(img, 'gray')
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
# 展示视频
def showvideo(cap, isgray=False):
	while(True):
		# ret：是否读取成功 frame：读取到图像(1帧)
		ret,frame = cap.read()
		if ret!=True:
			break
		# 变灰度
		if isgray:
			frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
		cv2.imshow('frame', frame)
		# waitKey 不断刷新(ms) 监控键盘输入 返回当前案件
		# ord返回对应的ASCII值
		if cv2.waitKey(40) & 0xff == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()

def facedetect(img):
    # 级联分类器
    detector = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
	# 1. image：输入图像 
	# 2. scaleFactor=1.1：这个是每次缩小图像的比例，默认是1.1 
	# 3. minNeighbors=3：匹配成功所需要的周围矩形框的数目，
	#		每一个特征匹配到的区域都是一个矩形框，只有多个矩形框同时存在的时候，
	#		才认为是匹配成功，比如人脸，这个默认值是3。 
	# 4. minSize：匹配人脸的最小范围 
	# 5. flags=0：可以取如下这些值：  
	# 	CASCADE_DO_CANNY_PRUNING=1, 利用canny边缘检测来排除一些边缘很少或者很多的图像区域
	# 	CASCADE_SCALE_IMAGE=2, 正常比例检测
	# 	CASCADE_FIND_BIGGEST_OBJECT=4, 只检测最大的物体
	# 	CASCADE_DO_ROUGH_SEARCH=8 初略的检测
    rects = detector.detectMultiScale(img, scaleFactor=1.1,
    	minNeighbors=2, minSize=(10,10), flags=cv2.CASCADE_SCALE_IMAGE)
    for (x,y,w,h) in rects:
        # 画矩形框
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
    return img
