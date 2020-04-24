from func import *

# 0代表摄像头读取 路径代表本地文件
capr = cv2.VideoCapture(0)

# 文件读取视频
cap = cv2.VideoCapture('../test/002.mp4')
# 帧数
fps = cap.get(cv2.CAP_PROP_FPS)
# 宽度
frm_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# 长度
frm_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(fps, frm_width, frm_height)

# 视频写入 DIVX,XVID,MJPG,X264,WMV1,WMV2
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('../test/out.avi', fourcc, fps, (frm_width,frm_height))

while (True):
	ret,frame = cap.read()
	if ret == True:	
		frame = cv2.flip(frame, 1) # 水平翻转
		out.write(frame)
		cv2.imshow('frame', frame)
		if cv2.waitKey(25) & 0xff == ord('q'):
			break
	else:
		break
out.release()
cap.release()
cv2.destroyAllWindows()


# showvideo(cap)

