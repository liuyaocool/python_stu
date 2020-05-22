import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
# 导入模块 
 
import warnings 
warnings.filterwarnings('ignore')  
# 不发出警告"


# z = sin(x+y)

from mpl_toolkits.mplot3d import axes3d
# 导入3d绘图包

X = np.linspace(-np.pi,np.pi,num = 50)
Y = np.linspace(-np.pi,np.pi,num = 50)
X, Y = np.meshgrid(X, Y)
Z = np.sin(X+Y)
#print(Z)

fig = plt.figure(figsize = (15,12))
ax = fig.gca(projection='3d')  
ax.view_init(elev=None, azim=None)
# 创建3d绘图空间
# view_init → 设置视角，elev设置z平面的角度，azim设置xy平面角度

ax.plot_surface(X, Y, Z, rstride=2, cstride=2,cmap='Blues',alpha = 0.9)
# rstride, cstride : 不同方向的采样距离"


# z = x**2 + 3*x*y + y**2

from mpl_toolkits.mplot3d import axes3d
# 导入3d绘图包

X = np.linspace(-5,5,num = 50)
Y = np.linspace(-5,5,num = 50)
X, Y = np.meshgrid(X, Y)
Z = X**2 + 3*X*Y + Y**2
#print(Z)

fig = plt.figure(figsize = (15,12))
ax = fig.gca(projection='3d')  
ax.view_init(elev=None, azim=None)
# 创建3d绘图空间
# view_init → 设置视角，elev设置z平面的角度，azim设置xy平面角度

#ax.plot_surface(X, Y, Z, rstride=2, cstride=2,cmap='Blues',alpha = 0.9)
ax.plot_wireframe(X, Y, Z, rstride=2, cstride=2,color = 'k',alpha = 0.8,linewidth = 0.5)  
ax.contourf(X, Y, Z, zdir='z', offset = -40, cmap='Blues',alpha = 0.7)
ax.contourf(X, Y, Z, zdir='x', offset = -6, cmap='Blues',alpha = 0.7)
ax.contourf(X, Y, Z, zdir='y', offset = 6, cmap='Blues',alpha = 0.7)
plt.xlim([-6,6])
plt.ylim([-6,6])
# 绘制曲面

ax.scatter(1,2,11, s=20,c = 'k')
# 曲面上的点(1,2,11)

def fxz(x):
    return 2**x + 6
xn1 = np.linspace(1,2,num = 20)
yn1 = np.ones_like(xn1)*2
zn1 = fxz(xn1)
ax.plot(xn1, yn1, zn1,'-r')
# 将y看成常量，则y=2，也就是在y=2这个面上，xz组成的函数求导

def fyz(y):
    return 2**y + 3
yn2 = np.linspace(2,3,num = 20)
xn2 = np.ones_like(xn1)*1
zn2 = fyz(yn2)
ax.plot(xn2, yn2, zn2,'-b')
# 将x看成常量，则x=1，也就是在x=1这个面上，yz组成的函数求导"

