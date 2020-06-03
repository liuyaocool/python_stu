
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
% matplotlib inline
# 导入模块

import warnings
warnings.filterwarnings('ignore') 
    # 不发出警告"

# 2.4.3 向量的性质
# * np.linalg.eigvals() → 计算矩阵的特征值
# * np.linalg.eig() → 返回包含特征值和对应特征向量的元组"

# 例子1

a = np.array([
        [3,-1],
        [-1,3]
    ])
print(np.linalg.eigvals(a))
print(np.linalg.eig(a))

# 例子2

a = np.array([
        [-1,1,0],
        [-4,3,0],
        [1,0,2]
    ])
print(np.linalg.eigvals(a))
print(np.linalg.eig(a))

# 2.4.4 矩阵的对角化
# * np.diag() → 对角化

a = np.array([
        [-2,1,1],
        [0,2,0],
        [-4,1,3]
    ])
print(np.linalg.eigvals(a)) 
# 得到特征值
np.diag(np.linalg.eigvals(a))
# 得到对角化矩阵
    