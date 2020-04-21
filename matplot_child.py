import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# 子图
fig = plt.figure(figsize=(10,6), facecolor='gray')

ax1 = fig.add_subplot(2,2,1) # 切换到 两行两列 第一张图 
plt.plot(np.random.rand(50).cumsum(), 'k--')

ax1 = fig.add_subplot(2,2,2) # 切换到 两行两列 第二张图 
plt.plot(np.random.rand(50).cumsum(), 'b--')

plt.show()


fig,axes = plt.subplots(2, 3, figsize=(10,4),
	sharex=True, sharey=True # 共享坐标轴
	)

ax1 = axes[0,1]
ts = pd.Series(np.random.randn(1000).cumsum())
ax1.plot(ts)

df = pd.DataFrame(np.random.randn(100, 2))
df.plot(ax=axes[1,0])

plt.show()