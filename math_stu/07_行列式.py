# n*n方阵

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 导入模块

import warnings
warnings.filterwarnings('ignore') 
# 不发出警告

# 行列式的计算 → numpy.linalg.det
# * 计算任何一个数组a的行列式，但是这里要求数组的最后两个维度必须是方阵"
# 练习1
d = np.array([
        [4,1,2,4],
        [1,2,0,2],
        [10,5,2,0],
        [0,1,1,7]
    ])
print(d)

np.linalg.det(d) # 计算行列式结果

# 练习2
def createD(a,x,n):
    # 构建函数，生成一个n阶的行列式，其中对角线值为x，其余为a
    di = np.eye(n)
    di = di * x
    di[di==0] = a
    return di

d = createD(5,20,10)
print(d)
np.linalg.det(d)
    