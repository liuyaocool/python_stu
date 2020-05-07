import matplotlib.pyplot as plt
import numpy as np

# 定义输入数据
X = np.array([
	[1,3,3],
	[1,4,3],
	[1,1,1],
	[1,2,1]
]);
# 定义标签
T = np.array([
	[1],
	[1],
	[-1],
	[-1]
]);
# 权值初始化
W = np.random.random([3,1])
# 学习率
lr = 0.1
# 神经网络输出
Y = 0
# 更新权值函数
def train():
    global X,Y,W,lr,T
    # 同时计算4个数据的预测值，Y(4，1)
    Y = np.sign(np.dot(X,W))
    # T-Y得到4个标签值与预测值的误差E(4，1)
    E = T - Y
    # 计算权值的变化
    delta_W = lr * (X.T.dot(E)) / X.shape[0]
    # 更新权值
    W = W +delta_W

# 训练模型
for i in range(100):
    # 更新权值
    train()
    # 打印当前训练次数
    print('epoch:',i+1)
    # 当前的权值
    print('weights:',W)
    # 计算当前输出
    Y = np.sign(np.dot(X,W))
    # all()表示Y中的所有值跟T中的所有值都对应相等，才为真
    if (Y == T).all():
        print('Finished')
        break

# 画图
# 正样本的xy坐标
x1 = [3,4]
y1 = [3,3]
# 负样本xy坐标
x2 = [1,2]
y2 = [1,1]
# 定义分类边界线的斜率和截距
k = -W[1]/W[2]
d = -W[0]/W[2]
# 设定两个点
xdata = (0,5)
# 通过两点来确定一条直线，用红色的线来画出分界线
plt.plot(xdata,xdata*k+d,'r')
# 用蓝色的点画正样本
plt.scatter(x1,y1,c='b')
# 用黄色的点画负样本
plt.scatter(x2,y2,c='y')
plt.show()








