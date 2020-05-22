import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
# 导入模块 
 
import warnings 
warnings.filterwarnings('ignore')  
# 不发出警告"



# 1.3.2 函数的单调性与曲线的凸凹性

# f(x) = 2*x**3 - 9*x**2 + 12*x - 3

def f1(x):
    return 2*x**3 - 9*x**2 + 12*x - 3   # 函数
def f1_1(x):
    return 6*x**2 -18*x + 12

n = np.linspace(-10,10,num = 100)
plt.plot(n,f1(n))
plt.plot(n,f1_1(n))

plt.axvline(0,color = 'gray',linestyle = '--',alpha=0.8)  
plt.axhline(0,color = 'gray',linestyle = '--',alpha=0.8)  
# 辅助线

#plt.xlim([-1,3])
#plt.ylim([-20,20])
# 查看x在[-1,3]区间的情况
# f1_(x) = 0时，x为1或2

# 结论：设函数y = f(x)在[a,b]上连续，在(a,b)内可导 → 若函数导数始终大于等于0，该函数单调增加；反之单调减少"
 
# 二阶导数

def f1_2(x):
    return 12*x - 18

n = np.linspace(-10,10,num = 100)
plt.plot(n,f1(n))
plt.plot(n,f1_1(n))
plt.scatter([1,2],[0,0],color = 'green')
plt.plot(n,f1_2(n))
plt.scatter([1.5],[0],color = 'red')

plt.xlim([-1,3])
plt.ylim([-20,20])
plt.axvline(0,color = 'gray',linestyle = '--',alpha=0.8)  
plt.axhline(0,color = 'gray',linestyle = '--',alpha=0.8)  
# 辅助线

# 结论：设函数y = f(x)在[a,b]上连续，在(a,b)内具有一阶和二阶导数 → 若函数二阶导数始终大于等于0，该函数在[a,b]上是凹函数；反之则是凸函数"
 

# 1.3.3 方程近似解


# 二分法求解
# 对于函数f(x) = x**3 + 1.1*x**2 + 0.9*x -1.4
# 单调递增

def f2(x):
    return x**3 + 1.1*x**2 + 0.9*x -1.4
def f2_1(x):
    return 3*x**2 + 2.2*x + 0.9

n = np.linspace(-10,10,num = 100)
plt.plot(n,f2(n))
plt.plot(n,f2_1(n))
plt.axvline(0,color = 'gray',linestyle = '--',alpha=0.8)  
plt.axhline(0,color = 'gray',linestyle = '--',alpha=0.8)  
# 辅助线

print('f(0)和f(1)的值分别为%.2f,%.2f' % (f2(0),f2(1)))
# f(0)=-1.4<0,f(1)=1.6>0,因此f(x)=0在[0,1]内有唯一实根"


# 二分法求解

lst = [0,1]
n = 0
while n < 30:
    z = (lst[0]+lst[1])/2
    if f2(z)*f2(0) > 0:   # 即与f(0)同号
        lst[0] = z
    else:
        lst[1] = z    
    print('第%i次迭代的隔离区间为' % (n+1),lst)
    n += 1

   # 切线法求解
# f ''(x) = 6 x + 2 经判断在区间[0, 1] f '(x)> 0, f ''(x)> 0, 因此f(x) = 0 至多一个实根。

def f2_2(x):
    return 6*x + 2.2

xmin = -0.2
xmax = 1.2
n = np.linspace(xmin,xmax,num = 100)
plt.plot(n,f2(n))
plt.xlim([xmin,xmax])
plt.ylim([f2(xmin),f2(xmax)])
plt.axvline(0,color = 'gray',linestyle = '--',alpha=0.8)  
plt.axvline(1,color = 'gray',linestyle = '--',alpha=0.8)  
plt.axhline(0,color = 'gray',linestyle = '--',alpha=0.8)  
# 辅助线

xn = 1
lst_k = []
for i in range(5):
    def f2_qx(xi):
        # 切线函数
        k = f2_1(xn)
        b = f2(xn) - k*xn
        return k*xi + b
    plt.plot(n,f2_qx(n))
    xn = xn - f2(xn)/f2_1(xn)
    print('第%i次迭代的近似值为'%i, xn)

