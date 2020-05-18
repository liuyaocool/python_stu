# BP神经网络
import matplotlib.pyplot as plt
import numpy as np

# 异或问题 =================================================================
# 输入数据
X = np.array([[1,0,0],
              [1,0,1],
              [1,1,0],
              [1,1,1]])
# 标签
Y = np.array([[0],
              [1],
              [1],
              [0]])
# 3-10-1
# 取值范围-1到1
V = np.random.random([3,10]) * 2 - 1
W = np.random.random([10,1]) * 2 - 1
# 学习率
lr = 0.11

def sigmoid(x):
    return 1/(1+np.exp(-x))

def dsigmoid(x):
    return x*(1-x)

# 权值调整函数
def update():
    global V,W
    
    # 求每一层的输出
    L1 = sigmoid(np.dot(X,V))
    L2 = sigmoid(np.dot(L1,W))
    
    # 求每一层的学习信号
    L2_delta = (Y-L2)*dsigmoid(L2)
    L1_delta = L2_delta.dot(W.T)*dsigmoid(L1)
    
    # 求每一层权值的变化
    delta_W = lr*L1.T.dot(L2_delta)
    delta_V = lr*X.T.dot(L1_delta)
    
    # 改变权值
    W = W + delta_W
    V = V + delta_V

for i in range(10001):
    # 更新权值
    update()
    if i%500==0:
        # 求每一层的输出
        L1 = sigmoid(np.dot(X,V))
        L2 = sigmoid(np.dot(L1,W))
        loss = np.mean(np.square(Y-L2)/2)
        print('loss:',loss)
L1 = sigmoid(np.dot(X,V))
L2 = sigmoid(np.dot(L1,W))
print(L2)

def judge(x):
    if x>=0.5:
        return 1
    else:
        return 0
    
for i in map(judge,L2):
    print(i)