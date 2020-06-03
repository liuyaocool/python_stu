
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 导入模块

import warnings
warnings.filterwarnings('ignore') 
# 不发出警告

np.arange(50).reshape(10,5)
# 构造一个10*5的矩阵"

np.eye(10)*10
# 10阶方阵，当对角线值为1时为对角矩阵
np.eye(5)

a = np.arange(10)
print(a)
print(a.shape)
# 行向量"

a = np.arange(10).reshape(10,1)
print(a)
print(a.shape)
# 列向量"

# 2.2.2 矩阵的运算"

ar1 = np.arange(12).reshape(3,4)
ar2 = np.arange(10,22).reshape(3,4)
ar3 = np.ones((3,4))
ar4 = np.ones((3,5))
print(ar1)
print(ar2)
print(ar3)
print(ar4)

# 矩阵加法

print(ar1+ar2)
print(ar1+ar2+ar3)
#print(ar1+ar4)
# shape需要相同"

# 数与矩阵相乘

ar1 * 10

# 数组与矩阵相乘

print(ar1*ar2) 
#print(ar1*ar4)
print('------')
# 数组相乘 → numpy里面两个shape相同的数组可以直接相乘，对应位置的值的乘积为结果
# 如果shape不同，则报错

a1 = np.array([2,3,4])
b1 = np.array([5,6,7]).reshape(3,1)  # 转换为列向量
c1 = np.dot(a1,b1)
print(a1.shape,b1.shape,c1.shape)
print(c1,type(c1))

a2 = np.array([
        [1,2,3],
        [2,3,4]
    ])
b2 = np.array([
        [4,4],
        [5,5],
        [6,6]
    ])
c2 = np.dot(a2,b2)
print(a2.shape,b2.shape,c2.shape)
print(c2)
# 矩阵乘法，需要保证第一个矩阵的列数（column）和第二个矩阵的行数（row）相同
# 设 A = (aij) 是一个m×s 矩阵, B = (bij)是一个s×n矩阵，那么规定矩阵A与矩阵B的乘积是一个m×n的矩阵
# 矩阵相乘结果仍为矩阵
# numpy中用.dop()来计算矩阵乘法"

# 矩阵乘法：A*B 与 B*A

a3 = np.array([
        [-2,4],
        [1,-2]
    ])
b3 = np.array([
        [2,4],
        [-3,-6]
    ])
print(np.dot(a3,b3))
print(np.dot(b3,a3))"

# 矩阵的转置

A = np.array([
        [2,0,-1],
        [1,3,2]
    ])
B = np.array([
        [1,7,-1],
        [4,2,3],
        [2,0,1]
    ])
np.dot(A,B).T

# 2.2.3 逆矩阵
# * 设A是数域上的一个n阶矩阵，若在相同数域上存在另一个n阶矩阵B，使得： AB=BA=E ，则我们称B是A的逆矩阵，而A则被称为可逆矩阵。注：E为单位矩阵 → 单位矩阵值为1
# * 唯一性：若矩阵A是可逆的，则A的逆矩阵是唯一的
# * A的逆矩阵的逆矩阵还是A。记作（A-1）-1=A
# * 可逆矩阵A的转置矩阵AT也可逆，并且（AT）-1=（A-1）T (转置的逆等于逆的转置）
# * 两个可逆矩阵的乘积依然可逆"

# 创建A矩阵

A = np.array([
        [1,2,3],
        [2,2,1],
        [3,4,3]
    ])
print(A)
print(np.linalg.det(A))

# numpy求逆矩阵B → np.linalg.inv()

B = np.linalg.inv(A)
print(B)
print(np.linalg.det(B))

# A*B = E，单位矩阵

E = np.dot(A,B)
print(E)
print(np.linalg.det(E))
#np.eye(3)"

# 伴随矩阵

A_bs = B*np.linalg.det(A)
print(A_bs)
print(np.linalg.det(A_bs))

# 练习1

a = np.array([
        [4,1,2,4],
        [1,2,0,2],
        [1,0,2,0],
        [0,1,1,0]
    ])

print(np.linalg.inv(a))
np.linalg.det(a)

# 练习2

a = np.array([
        [1,1,1],
        [1,2,4],
        [1,3,9]
    ])
a1 = np.array([
        [2,1,1],
        [3,2,4],
        [5,3,9]
    ])
a2 = np.array([
        [1,2,1],
        [1,3,4],
        [1,5,9]
    ])
a3 = np.array([
        [1,1,2],
        [1,2,3],
        [1,3,5]
    ])

x1 = np.linalg.det(a1)/np.linalg.det(a)
x2 = np.linalg.det(a2)/np.linalg.det(a)
x3 = np.linalg.det(a3)/np.linalg.det(a)

print('该方程的三个根为：x1=%.2f, x2=%.2f, x3=%.2f' % (x1,x2,x3))
    