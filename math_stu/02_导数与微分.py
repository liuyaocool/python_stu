import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
# 导入模块 
 
import warnings 
warnings.filterwarnings('ignore')  
# 不发出警告"


# 1.2.1 导数


# 直线运动问题 
# 对于f(X) = x**2 
 
def f(x): 
   return x**2 
 
plt.figure(figsize = (12,6)) 
n = np.linspace(-10,10,num = 50) 
plt.plot(n,f(n)) 
plt.xlim(-11,11) 
plt.ylim(-10,110) 
 
# 选中曲线上两个点，m(2,4)，n(5,25) 
plt.plot([2,5],[4,25],color = 'r') 
print('直线斜率为%.2f' % ((25-4)/(5-2))) 
print('-------')

 # 求m的导数 
 
x_m = 2 
y_m = f(x_m) 
plt.plot(n,f(n)) 
plt.xlim(1,7) 
plt.ylim(1,49) 
 
for i in range(4,0,-1): 
    plt.plot([x_m,x_m + i],[y_m,f(x_m + i)],color = 'r') 
    print('直线斜率为%.2f' % ((f(x_m + i)-y_m)/(x_m + i-x_m))) 
 
# f(x) = x**2 
# 原始点 m,f(m) 
# 增量为i,直线终点 → m+i,f(m+i) 
# 斜率 → (f(m+i)-f(m))/i"

def ds(xm,n): 
	''' 
	该函数为求f(x) = x**2的导数 
	xm：m点的x值 
	n：m点x往右偏移的距离 
	函数最后导出 → m点与m偏移n距离后点的连线的斜率 
	''' 
	y1 = f(xm) 
	y2 = f(xm+n) 
	return (y2-y1)/n 
 
for i in np.linspace(1,0,num = 1000,endpoint = False): 
	print('偏移%.2f个单位距离时，斜率为：%.5f' % (i,ds(2,i))) 
# 斜率为4 
# 切线函数为：y = 4*x - 4"

  # 图示 
 
n = np.linspace(-10,10,num = 50) 
plt.plot(n,f(n)) 
plt.xlim(-11,11) 
plt.ylim(-10,110) 
 
plt.scatter(2,4) 
plt.plot(n,4*n - 4) 
# m点切线"

def f(x): 
   return 2*x**3 - 5*x**2 +3*x*np.sin(x)+(x**2 +1)/(2*x) - 7 
 
x = np.linspace(0,10,num = 100) 
y = f(x) 
plt.figure(figsize = (12,6)) 
#plt.scatter(x,y) 
plt.plot(x,y) 
 
 
def f_(x): 
    return 1 - 10*x +6*x**2 -(1+x**2)/(2*x**2) + 3*np.cos(x)*x +3*np.sin(x) 
 
m = 6 
ym = f(6) 
print(m,ym) 
plt.scatter(m,ym) 
 
k = f_(6) 
b = ym - m*k 
 
def fk(x): 
	return k*x+b 
 
yk = fk(x) 
plt.plot(x,yk)

def f2(x): 
    return x**3 
def f2_(x): 
    return 3*x**2 
def f2__(x): 
    return 6*x 
plt.figure(figsize = (12,6)) 
x = np.linspace(-10,10,num = 50) 
y1 = f2(x) 
plt.plot(x,y1) 
plt.plot(x,f2_(x)) 
plt.plot(x,f2__(x))