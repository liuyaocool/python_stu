# 形态学
from func import *

img = imgread('lovely.jpg')
(R,G,B) = cv2.split(img)

ken1 = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5)) # 矩形
print(ken1)
ken2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5)) # 椭圆
print(ken2)
ken3 = cv2.getStructuringElement(cv2.MORPH_CROSS, (5,5)) # 十字形
print(ken3)

# Erosion腐蚀 取区域最小值 白色减弱
img1 = img.copy()
for i in range(3):
	img1 = cv2.erode(img1, ken3, iterations=i+1)

# Dilation膨胀 取区域最大值 白色增大
img2 = img.copy()
for i in range(3):
	img2 = cv2.dilate(img2, ken3, iterations=i+1)

# Opening开运算 先腐蚀后膨胀 去除白点
img3 = cv2.morphologyEx(img, cv2.MORPH_OPEN, ken1)
# Closing开运算 先膨胀后腐蚀 去除黑点
img4 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, ken1)
# Gradient形态学梯度 轮廓
img5 = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, ken1)
# 白帽
img6 = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, ken1)
# 黑帽
img7 = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, ken1)


# showimg(img7)


# 图像平滑 ===================================================
zeros = np.zeros(img.shape[:2],dtype='uint8')
plt.figure(figsize=(15,15))
# Averaging 平均
# for i,ken in enumerate([(3,3), (9,9), (15,15)]):
# 	plt.subplot(1, 3, i+1)
# 	# 平均平滑
# 	blur = cv2.blur(img, ken)
# 	plt.axis('off')
# 	# 设置标题
# 	plt.title('blur'+str(ken))
# 	plt.imshow(blur)
# plt.show()

# Gaussian 高斯模糊 加权平均
# for i,ken in enumerate([(3,3), (9,9), (15,15)]):
# 	plt.subplot(1, 3, i+1)
# 	blur = cv2.GaussianBlur(img, ken, 0) # 0：标准差
# 	plt.axis('off')
# 	plt.title('GaussianBlur'+str(ken))
# 	plt.imshow(blur)
# plt.show()

# Median 中值模糊
# for i,ken in enumerate((3, 9, 15)):
# 	plt.subplot(1, 3, i+1)
# 	blur = cv2.medianBlur(img, ken)
# 	plt.axis('off')
# 	plt.title('medianBlur'+str(ken))
# 	plt.imshow(blur)
# plt.show()

# Bilateral 双边滤波 
# p = [(11, 21, 7), (11, 41, 2), (15, 75, 75)]
# # 领域直径 灰度值相似性高斯函数标准差 空间高斯函数标准差
# for i,(dia, sigc, sigs) in enumerate(p):
# 	plt.subplot(1, 3, i+1)
# 	blur = cv2.bilateralFilter(img, dia, sigc, sigs)
# 	plt.axis('off')
# 	plt.title('bilateralFilter'+str((dia, sigc, sigs)))
# 	plt.imshow(blur)
# plt.show()

# 颜色空间转换 ===================================================

# RGB
# for i in range(3):
# 	plt.subplot(1, 3, i+1)
# 	a = [zeros,zeros,zeros]
# 	a[i] = [R,G,B][i]
# 	imggg = cv2.merge(a)
# 	plt.axis('off')
# 	plt.imshow(imggg)
# plt.show()

# HSV H色调 S饱和度 V明度
# hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
# for(name,chan) in zip(('H', 'S', 'V'), cv2.split(hsv)):
# 	cv2.imshow(name,chan)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# L*A*B L:明度 A:正红负绿 B:正黄负蓝
# lab = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
# for(name,chan) in zip(('L', 'A', 'B'), cv2.split(lab)):
# 	cv2.imshow(name,chan)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Grayscale 灰度
img2 = cv2.imread('lovely.jpg')
gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
