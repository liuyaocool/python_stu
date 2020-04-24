# 二值化
from func import *

img = imgread('lovely.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# 127阈值
ret1,thresh1 = cv2.threshold(gray, 200, 255,cv2.THRESH_BINARY)
ret2,thresh2 = cv2.threshold(gray, 127, 255,cv2.THRESH_BINARY_INV)
ret3,thresh3 = cv2.threshold(gray, 127, 255,cv2.THRESH_TRUNC)
ret4,thresh4 = cv2.threshold(gray, 127, 255,cv2.THRESH_TOZERO)
ret5,thresh5 = cv2.threshold(gray, 127, 255,cv2.THRESH_TOZERO_INV)

titles = ['original','THRESH_BINARY','THRESH_BINARY_INV','THRESH_TRUNC',
'THRESH_TOZERO','THRESH_TOZERO_INV']
imgs = [gray, thresh1, thresh2, thresh3, thresh4, thresh5] 
plt.figure(figsize=(15,5))

# for i in range(6):
# 	plt.subplot(2,3,i+1)
# 	plt.imshow(imgs[i], 'gray')
# 	plt.title(titles[i])
# 	plt.axis('off')
# plt.show()

# showimg(cv2.bitwise_and(img,img,mask=thresh1))

# Otsu's method 自动选择阈值 =================================

ret6,thresh6 = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
ret7,thresh7 = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
print(ret6, ret7)
# showgray(thresh7)

# Adaptive Thresholding 自适应阈值 ===================================
medianImg = cv2.medianBlur(gray, 5)
# 普通二值化
ret8,th8 = cv2.threshold(gray, 127, 255,cv2.THRESH_BINARY)
# 平均值阈值
th9 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 3)
# 高斯阈值
th10 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 3)
titles = ['original', 'THRESH_BINARY', 'ADAPTIVE_THRESH_MEAN_C', 'ADAPTIVE_THRESH_GAUSSIAN_C']
imgs = [img, th8, th9, th10]
for i in range(4):
	plt.subplot(2,2,i+1)
	plt.imshow(imgs[i],'gray')
	plt.axis('off')
	plt.title(titles[i])
plt.show()
