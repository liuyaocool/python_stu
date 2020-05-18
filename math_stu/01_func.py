import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 导入模块

import warnings
warnings.filterwarnings('ignore') 
# 不发出警告

# 基本初等函数：幂函数
# f(x) = x**a

x = np.linspace(-np.pi,2*np.pi,num = 50)
y = x**2 # 比如y等于x的二次幂

plt.scatter(x,y,marker = '.')
plt.plot(x,y)
# 辅助线
plt.axvline(0,color = 'gray',linestyle = '--',alpha=0.8)  
plt.axhline(0,color = 'gray',linestyle = '--',alpha=0.8)  

# 基本初等函数：指数函数
# f(x) = a**x
x = np.linspace(-np.pi,2*np.pi,num = 50)
y = 2**x  # 底数为2的指数函数

plt.scatter(x,y,marker = '.')
plt.plot(x,y)

# 辅助线
plt.axvline(0,color = 'gray',linestyle = '--',alpha=0.8)  
plt.axhline(0,color = 'gray',linestyle = '--',alpha=0.8)  

 # 基本初等函数：对数函数
# f(x) = loga(x)

x = np.linspace(-np.pi,2*np.pi,num = 50)
y = np.log2(x)

plt.scatter(x,y,marker = '.')
plt.plot(x,y)

plt.axvline(0,color = 'gray',linestyle = '--',alpha=0.8)  
plt.axhline(0,color = 'gray',linestyle = '--',alpha=0.8)  
# 辅助线

 # 基本初等函数：三角函数
# f(x) = sin(ax)

x = np.linspace(-np.pi,2*np.pi,num = 50)
y = np.cos(x)

plt.scatter(x,y,marker = '.')
plt.plot(x,y)

plt.axvline(0,color = 'gray',linestyle = '--',alpha=0.8)  
plt.axhline(0,color = 'gray',linestyle = '--',alpha=0.8)  
# 辅助线

 # 基本初等函数：反三角
# f(x) = arcsin(ax)

x = np.linspace(-1,1,num = 50)
y = np.arcsin(x)

plt.scatter(x,y,marker = '.')
plt.plot(x,y)

plt.axvline(0,color = 'gray',linestyle = '--',alpha=0.8)  
plt.axhline(0,color = 'gray',linestyle = '--',alpha=0.8)  
# 辅助线


#1.1.2 数列

# 一列有序的数
# 数列中的每一个数都叫做这个数列的项。
# 排在第一位的数称为这个数列的第1项（通常也叫做首项）
# 排在第二位的数称为这个数列的第2项，以此类推，
#	排在第n位的数称为这个数列的第n项，通常用an表示

s = []
for n in range(1,11):
    s.append('%i/%i' % (n,n+1))
# 这里为了显示所以用字符串表示

# 数列的极限 → 如果存在常数a对任意给定的正数ε,不论这个数多么小，
#  	总存在正整数N，使得当 n>N时，不等式|An -a|<ε都成立，
# 那么常数a是数列 {An} 的极限

x = np.arange(50)
y = x/(x+1)

plt.scatter(x,y,marker = '.')
plt.plot(x,y)

plt.axvline(0,color = 'gray',linestyle = '--',alpha=0.8)  
plt.axhline(0,color = 'gray',linestyle = '--',alpha=0.8)  
# 辅助线

plt.axhline(1,color = 'red',alpha=0.8)  
# 极限值为1


#1.1.3 函数的极限

  # 无穷远处，函数的极限 x → ∞
# 特定值，函数的极限
# f(x) = x/(x+1)
# f(x) = x**2 - 1

x = np.linspace(-2,2,num = 50)
y = x**2 - 1

plt.scatter(x,y,marker = '.')
plt.plot(x,y)

plt.axvline(0,color = 'gray',linestyle = '--',alpha=0.8)  
plt.axhline(0,color = 'gray',linestyle = '--',alpha=0.8)  
# 辅助线

plt.axhline(-1,color = 'red',alpha=0.8)  
# 极限值为-1


#练习：计算下列极限
# 练习1
# f(x) = (2*x+1)/x

x = np.arange(50)
y = (2*x+1)/x

plt.scatter(x,y,marker = '.')
plt.plot(x,y)

plt.axhline(2,color = 'red',alpha=0.8)  
# x无穷远，极限值为2


# 练习2
# f(x) = (1-x**2)/(1-x)

x = np.linspace(10,1,num = 50)
y = (1-x**2)/(1-x)

plt.scatter(x,y,marker = '.')
plt.plot(x,y)

plt.axhline(2,color = 'red',alpha=0.8)  
# x趋近1，极限值为2
# 这里是间断函数，如果补充定义f(x) = 2(x=1时），则为连续函数

plt.show()
