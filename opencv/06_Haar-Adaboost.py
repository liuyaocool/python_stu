# Haar特征 Adaboost级联分类器
from func import *

img = imgread('lovely.jpg')

detector = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

rects = detector.detectMultiScale(img, scaleFactor=1.1, 
	minNeighbors=2, minSize=(10,10), flags=cv2.CASCADE_SCALE_IMAGE)
for (x,y,w,h) in rects:
    #画矩形框
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

img2 = facedetect(img)
showimg(img2)