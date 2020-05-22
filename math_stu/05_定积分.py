import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
# 导入模块 
 
import warnings 
warnings.filterwarnings('ignore')  
# 不发出警告"


# 1.5.2 定积分的求解


# 计算定积分

def f(x):
    return x**2

n = np.linspace(-1,2,num = 50)
n1 = np.linspace(0,1,num = 50)
plt.plot(n,f(n))
plt.fill_between(n1,0,f(n1),color = 'k',alpha = 0.4)
plt.xlim(-1,2)
plt.ylim(-1,5)

plt.axvline(0,color = 'gray',linestyle = '--',alpha=0.8)  
plt.axvline(1,color = 'gray',linestyle = '--',alpha=0.8)  
plt.axhline(0,color = 'gray',linestyle = '--',alpha=0.8)  
# 辅助线

area = 0
xi = 0
for i in range(len(n1))[:-1]:
    xi = (n1[i]+n1[i+1])/2
    area += (n1[i+1]-n1[i])*f(xi)
print(area)
# 计算0-1上的定积分值"


# 1.5.3 定积分的应用


# 计算图形面积

def f11(x):
    return (2*x)**0.5
def f12(x):
    return -(2*x)**0.5
def f2(x):
    return x - 4

n = np.linspace(10,-2,num = 100)
plt.plot(n,f2(n))

n1 = n[n>=0]
plt.plot(n1,f11(n1))
plt.plot(n1,f12(n1))
plt.xlim(-2,10)
plt.axvline(0,color = 'gray',linestyle = '--',alpha=0.8)  
# 辅助线

y = np.linspace(-2,4,num = 100)
area = 0
for i in range(len(y))[:-1]:
    y_ = y[i+1]-y[i]
    area += y_ * (y[i+1] + 4 - y[i+1]**2/2)
print(area)
# 计算[-2,4]上的定积分值"


# 练习1

def f(x):
    return (x + np.sin(x))/(1+np.cos(x))

n = np.linspace(-1,0.8*np.pi,num = 50)
n1 = np.linspace(0,0.5*np.pi,num = 50)
plt.plot(n,f(n))
plt.fill_between(n1,0,f(n1),color = 'k',alpha = 0.4)
plt.xlim(-1,0.8*np.pi)
plt.ylim(-1,4)

plt.axvline(0,color = 'gray',linestyle = '--',alpha=0.8)  
plt.axvline(0.5*np.pi,color = 'gray',linestyle = '--',alpha=0.8)  
plt.axhline(0,color = 'gray',linestyle = '--',alpha=0.8)  
# 辅助线

area = 0
xi = 0
for i in range(len(n1))[:-1]:
    xi = (n1[i]+n1[i+1])/2
    area += (n1[i+1]-n1[i])*f(xi)
print(area)
# 计算0-0.5*np.pi上的定积分值"


# 练习2

def f(x):
    return (1 - np.sin(2*x))**0.5

n = np.linspace(-1,0.4*np.pi,num = 50)
n1 = np.linspace(0,0.25*np.pi,num = 50)
plt.plot(n,f(n))
plt.fill_between(n1,0,f(n1),color = 'k',alpha = 0.4)
plt.xlim(-0.5,0.4*np.pi)
plt.ylim(-1,2)

plt.axvline(0,color = 'gray',linestyle = '--',alpha=0.8)  
plt.axvline(0.25*np.pi,color = 'gray',linestyle = '--',alpha=0.8)  
plt.axhline(0,color = 'gray',linestyle = '--',alpha=0.8)  
# 辅助线

area = 0
xi = 0
for i in range(len(n1))[:-1]:
    xi = (n1[i]+n1[i+1])/2
    area += (n1[i+1]-n1[i])*f(xi)
print(area)
# 计算0-0.25*np.pi上的定积分值"

