

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
% matplotlib inline
# 导入模块

import warnings
warnings.filterwarnings('ignore') 
    # 不发出警告

    # 2.3.1 矩阵变换

a = np.array([
        [2,-1,-1,1],
        [1,1,-2,1],
        [4,-6,2,-2],
        [3,6,-9,7]
    ])
a1 = np.array([
        [2,-1,-1,1],
        [4,1,-2,1],
        [4,-6,2,-2],
        [9,6,-9,7]
    ])
a2 = np.array([
        [2,2,-1,1],
        [1,4,-2,1],
        [4,4,2,-2],
        [3,9,-9,7]
    ])
a3 = np.array([
        [2,-1,2,1],
        [1,1,4,1],
        [4,-6,4,-2],
        [3,6,9,7]
    ])
a4 = np.array([
        [2,-1,-1,2],
        [1,1,-2,4],
        [4,-6,2,4],
        [3,6,-9,9]
    ])

x1 = np.linalg.det(a1)/np.linalg.det(a)
x2 = np.linalg.det(a2)/np.linalg.det(a)
x3 = np.linalg.det(a3)/np.linalg.det(a)
x4 = np.linalg.det(a4)/np.linalg.det(a)

print('该方程的四个根为：x1=%.2f, x2=%.2f, x3=%.2f, x4=%.2f' % (x1,x2,x3,x4))

a = np.array([
        [0,-2,1],
        [3,0,-2],
        [-2,3,0]
    ])

print(np.linalg.inv(a))
np.linalg.det(a)

    # 2.3.2 线性方程组

# 计算秩

a = np.array([
        [1,2,3],
        [2,3,-5],
        [4,7,1]
    ])
b = np.array([
        [3,2,0,5,0],
        [3,-2,3,6,-1],
        [2,0,1,5,-3],
        [1,6,-4,-1,4]
    ])
r1 = np.linalg.matrix_rank(a)
r2 = np.linalg.matrix_rank(b)

print(r1,r2)

# 例子
a = np.array([
        [1,2,2,3],
        [2,1,-2,-2],
        [1,-2,-4,-3]
    ])
ab = np.array([
        [1,2,2,3,0],
        [2,1,-2,-2,0],
        [1,-2,-4,-3,0]
    ])
n = 4
ra = np.linalg.matrix_rank(a)
rab = np.linalg.matrix_rank(ab)

print(n,ra,rab)

# 练习1

a = np.array([
        [3,-2,0,-1],
        [0,2,2,1],
        [1,-2,-3,-2],
        [0,1,2,1]
    ])

print(np.linalg.inv(a))
np.linalg.det(a)

# 练习2 (1)

a = np.array([
        [1,1,2,-1],
        [2,1,1,-1],
        [2,2,1,2]
    ])
ab = np.array([
        [1,1,2,-1,0],
        [2,1,1,-1,0],
        [2,2,1,2,0]
    ])
n = 4
ra = np.linalg.matrix_rank(a)
rab = np.linalg.matrix_rank(ab)

print(n,ra,rab)

# 练习2 (2)

a = np.array([
        [4,2,-1],
        [3,-1,2],
        [11,3,0]
    ])
ab = np.array([
        [4,2,-1,2],
        [3,-1,2,10],
        [11,3,0,8]
    ])
n = 4
ra = np.linalg.matrix_rank(a)
rab = np.linalg.matrix_rank(ab)

print(n,ra,rab)

    