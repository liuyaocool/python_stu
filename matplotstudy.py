import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# % matplotlib inline # 静态
# % matplotlib nootbook # 可交互
# % matplotlib qt5 # 弹出可交互

# plt.plot(np.random.rand(10))

df = pd.DataFrame(np.random.rand(10, 2), columns=['A','B'])
fig = df.plot(figsize=(6,4), title='test')
# plt.title('test2')
plt.xlabel('xlabel')
plt.ylabel('ylabel')

# 图例
plt.legend(loc='upper right') 
# best\lower left\right\center left\lower center\center

plt.xlim([2,6]) # x坐标区间
plt.ylim([0.2, 0.7])
plt.xticks(range(15)) # x刻度
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2])
plt.grid(True, linestyle="--",color="green",linewidth="0.5",axis="y") # 网格线
fig.set_xticklabels("%.1f" %i for i in range(10)) # x刻度标签

plt.tick_params(bottom='off',top='on',left='off',right='on') #刻度显示

import matplotlib
matplotlib.rcParams['xtick.direction'] = 'in' # ytick.direction: out\inout

# plt.axis('off') 
frame = plt.gca()
frame.axes.get_xaxis().set_visible(True)
frame.axes.get_yaxis().set_visible(False)

plt.text(5, 0.5, 'sign', fontsize=10)
# plt.savefig("C:/Users/liuyao/Desktop/python/test/plt.png",
	# dpi=400, bbox_inches='tight',facecolor='g',edgecolor='b')

# 参数
# linestyle:-.\-\--\.\:\ 
# lintwidth 先宽度
# marker: . o v < > 1 2 3 4 s p * h H + x D d / _ 
# s 点尺寸
# alpha 透明度
# color 
# colormap 颜色渐变 颜色带
# style = linestyle+marker+color
# marplot 风格

plt.show()
