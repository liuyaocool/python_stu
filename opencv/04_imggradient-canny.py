from func import *

img = imgread('lovely.jpg')

# 图像梯度
def gradient(img):
	gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
	# cv2.CV_64F:输出图像的深度(数据类型),64位float,因为梯度可正可负
	laplacian = cv2.Laplacian(gray, cv2.CV_64F)
	# 1,0:表示在x方向求1阶导数，最大可2阶
	sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
	# 0,1:表示在y方向求1阶导数，最大可2阶
	sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
	titles = ['origianal','laplacian','sobelx','sobely']
	imgs = [gray, laplacian, sobelx, sobely]
	for i in range(4):
		plt.subplot(2,2,i+1)
		plt.imshow(imgs[i],'gray')
		plt.axis('off')
		plt.title(titles[i])
	plt.show()

# gradient(img)

# Canny 边缘监测
def edge_detection(img, minval=100,maxval=200):
	gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
	edges = cv2.Canny(gray, minval, maxval)
	showgray(edges)

edge_detection(img)
edge_detection(img, 50, 50)

