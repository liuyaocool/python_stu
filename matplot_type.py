import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ts.plot(
# 	kind="line", # bar\barh\kde\
# 	label='label',
# 	style='--r',
# 	color='red',
# 	alpha=0.4,
# 	use_index=True, # 是否刻度标签
# 	rot=45, # 刻度旋转
# 	grid=True, 
# 	ylim=[-50,50],
# 	yticks=list(range(-50,50,10)),
# 	figsize=(8,4),
# 	title='test',
# 	legend=True # 是否有图例
# 	)

fig,axes = plt.subplots(3, 4, figsize=(12, 5),sharex=True, sharey=True )

df = pd.DataFrame(np.random.randn(100, 2))
df.plot(ax=axes[1,0])



plt.show()