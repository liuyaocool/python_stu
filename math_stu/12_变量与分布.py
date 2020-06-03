

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
% matplotlib inline
# 导入模块

import warnings
warnings.filterwarnings('ignore') 
# 不发出警告"

# 数据分布的图表可视化 - 直方图

r = np.random.RandomState(1)
ar = r.randn(1000) * 100  # 创建一个正态分布数组

plt.hist(ar,bins = 50)
plt.grid()

# 数据分布的图表可视化 - 箱型图

plt.boxplot(ar,
            vert = True,  # 是否垂直
            whis = 1.5,  # IQR，默认1.5，也可以设置区间比如[5,95]，代表强制上下边缘为数据95%和5%位置
            patch_artist = True,  # 上下四分位框内是否填充，True为填充
            meanline = False,showmeans=True,  # 是否有均值线及其形状
            showbox = True,  # 是否显示箱线
            showcaps = True,  # 是否显示边缘线
            showfliers = True,  # 是否显示异常值
            notch = False,  # 中间箱体是否缺口
            )
plt.grid()

# 计算分位数

df = pd.DataFrame(ar,columns = ['value'])
q25 = df['value'].quantile(0.25)
q40 = df['value'].quantile(0.4)
q75 = df['value'].quantile(0.75)
print('df的25分位数为%.2f, 40分位数为%.2f, 75分位数为%.2f' % (q25,q40,q75))
print('df的中位数为%.2f' % df['value'].median())
print('-------')
# pandas中为.quantile()

a25 = np.percentile(ar,25)
a40 = np.percentile(ar,40)
a75 = np.percentile(ar,75)
print('ar的25分位数为%.2f, 40分位数为%.2f, 75分位数为%.2f' % (a25,a40,a75))
# numpy中为.percentile()"
    