# 卷积核

from func import *

img = imgread('lovely.jpg')

(h,w,c) = img.shape
cx,cy = (w//2,h//2)
print('center:',cx,cy)

# cv2.imwrite('mylovely.jpg', img) # 保存

(b1,g1,r1) = img[0,0]
print('img[0,0]:', b1,g1,r1)

# 修改颜色
img[0,0] = (0,0,255)
img1 = img.copy()
img1[0:cy, 0:cx] = (123,234, 161)

# 剪切
img2 = img[0:cy,0:cx]

# 平移 1,0:水平方向 222像素 0,1:竖直方向 500像素
M = np.float32([[1,0,-222], [0,1,500]])
img3 = cv2.warpAffine(img, M, (w,h))

# 旋转 (cx,cy)中心点 45:逆时针45度(-45:顺时针) 1.0：缩放 
M = cv2.getRotationMatrix2D((cx, cy), 45, 1.0)
img4 = cv2.warpAffine(img, M, (w,h))

# 重新设置尺寸
img5 = cv2.resize(img, (80,192))
# 尺寸算法 5种 
# 最邻近 cv2.INTER_NEAREST
# 双线性 cv2.INTER_LINEAR
# 基于像素区域 cv2.INTER_AREA
# 立方插值 cv2.INTER_CUBIC
# 兰索斯插值 cv2.INTER_LANCZOS4
img5 = cv2.resize(img, (80,192), interpolation=cv2.INTER_NEAREST)

# 级联分类器
# det cv2.CascadeClassifier('xxx.xml')
# img6 = det.detectMulitiSacle()

# 翻转 1:水平 0:垂直 -1:水平+垂直
img7 = cv2.flip(img, 1)

# 画图
img8 = np.zeros((300,300,3), dtype='uint8')
print('info -- w:%dpx, h:%dpx, chnl:%d' %(img8.shape))
(h,w,c) = img8.shape
cx,cy = (w//2,h//2)
print('img8-center:',cx,cy)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)

# 画线 参数：启始点 结束点
cv2.line(img8, (0,0), (300, 300), green)
cv2.line(img8, (0,300), (100, 100), blue, 5)

# 矩形 参数：左上方点 右下方点
cv2.rectangle(img8, (10,10), (60,60), red, 3)
cv2.rectangle(img8, (70,70), (90,90), red, -1)

# 圆形 (20,70):圆心 12:半径 2:线粗细
cv2.circle(img8, (20,70), 12, white, 2)
cv2.circle(img8, (40,90), 12, white, -1)

# 图像算术
print(cv2.add(np.uint8([200]), np.uint8([100])))
print(np.uint8([200]) + np.uint8([100]))
print(cv2.subtract(np.uint8([20]), np.uint8([100])))
print(np.uint8([20]) - np.uint8([100]))
# 生成跟图片形状相同的并且全为100的数据
M = np.ones(img.shape, dtype='uint8') * 100
img8 = cv2.add(img, M)
img9 = cv2.subtract(img, M)

# 按位运算
rect = np.zeros((300,300,3), dtype='uint8')
circle = rect.copy()
cv2.rectangle(rect, (25,25), (275,275), white, -1)
cv2.circle(circle, (150,150), 148, white, -1)

img10 = cv2.bitwise_and(rect,circle)
img11 = cv2.bitwise_or(rect,circle)
img12 = cv2.bitwise_xor(rect,circle)
img13 = cv2.bitwise_not(circle) # 反转

# 遮挡
mask = np.zeros(img.shape, dtype='uint8')
cv2.rectangle(mask, (50,50), (250,250), white, -1)
img14 = cv2.bitwise_and(img, mask)

# 切分
(R,G,B) = cv2.split(img)
# 合并
img15 = cv2.merge([B,R,G])
# cv2.imshow('R',R)
# cv2.imshow('G',G)
# cv2.imshow('B',B)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 高斯金字塔
img16 = img.copy()
for i in range(4):
	img16 = cv2.pyrDown(img16);
print(img16.shape)
img17 = img16.copy()
for i in range(4):
	img17 = cv2.pyrUp(img17)
print(img17.shape)

# 拉普拉斯金字塔
a = cv2.pyrDown(img)
b = cv2.pyrDown(a)
c = cv2.pyrUp(b)
img18 = a - c;


showimg(img18)