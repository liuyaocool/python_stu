import numpy as np
import pandas as pd

print("")
print("================= Series 1D ============================================")
# 索引
rng = np.random.RandomState(1)
ar = rng.rand(5)
s = pd.Series(ar)
print(ar)
print(s, type(s))
print(s.index, type(s.index))
s = pd.Series([67, 89, 99], index= ["Jone", "Mary", "Bob"])
print(s)
s = pd.Series({'a':1, 'b':2}, dtype=np.object)
print(s)
s = pd.Series({'a':1, 'b':2}, dtype=np.object, name='test')
print(s)
s.rename("tt")
print(s)
print(s.rename("tt"))

print("================= DataFrame 2D ============================================")
# 表格形
print("--------------- create 1 ---------------")
data = {
	'name': ["Jone", "Mary", "Bob"],
	'age': [31, 32, 33]
}
frame = pd.DataFrame(data,index=['a','b','c'])
print(frame)
print(type(frame))
print("index:",frame.index, type(frame.index))
print("columns:",frame.columns, frame.columns.tolist())
print("values:\n",frame.values, frame.values.tolist())
print(frame.columns.tolist())
print("--------------- create 2 ---------------")
data1 = {
	'a': np.random.rand(3),
	'b': np.random.rand(3),
	'c': np.random.rand(3)
}
f = pd.DataFrame(data1, columns = ['a','b','c','d'])
print(f)
f['e'] = 100;
print(f)
del f['d']
print(f)
f = pd.DataFrame(data1, index = ['q','w','e'])
print(f)
d = {
	'aa': pd.Series(np.random.rand(2)),
	'bb': pd.Series(np.random.rand(3))
}
f = pd.DataFrame(d)
print(f)
d = {
	'aa': pd.Series(np.random.rand(2), index = ['a', 'b']),
	'bb': pd.Series(np.random.rand(3), index = ['a', 'b', 'c'])
}
f = pd.DataFrame(d)
print(f)
print("--------------- create 3 ---------------")
ar = np.random.rand(12).reshape(3,4)
f = pd.DataFrame(ar)
print(f)
f = pd.DataFrame(ar, index=['a','b','c'], columns=['aa','bb','cc', 'dd'])
print(f)

print("================= DataFrame index/cut ============================================")
ar = np.random.rand(12).reshape(3,4)
f = pd.DataFrame(ar, index=['a','b','c'], columns=['aa','bb','cc', 'dd'])
print(f)
print('------------------- loc ----------------------')
print('----------- index ---------------')
print(f['aa'])
print(f[['aa','bb']]) # 两个中括号选择多个
print(f.loc['a'])
print(f.loc[['a','b']])
print('----------- cut ---------------')
print(f.loc['a':'c'])
print(f[['aa', 'cc']].loc['a':'c'])
print('------------------- iloc ----------------------')
# 按照行号索引
print(f.iloc[[0, 2]])
print(f.iloc[:2])
print('------------------- bool index ----------------------')
print(f[f['aa'] > 0.42]) # 索引aa列大于***

print("================= DataFrame skill ============================================")
print(f.head(2))  
print(f.tail(2)) 
print(f.T) 
print('--------------- update --------------')
f['cc'] = 111
f[['aa', 'dd']] = 101
f['ee'] = 11
print(f)
f.iloc[0] = 112
f.iloc[1] = [1,2,3,4,5]
f.loc['d'] = 20
print(f)
print('--------------- del/drop --------------')
del f['aa']
print(f)
f.drop('a', inplace=True)
print(f)
f.drop(['b','c'], axis=0, inplace=True) # 0删除行 1 删除列
print(f)
print('--------------- + --------------')
f1 = pd.DataFrame(np.random.rand(3,4),columns=['a','b','c','d'])
f2 = pd.DataFrame(np.random.rand(6,3),columns=['a','b','c'])
print(f1)
print(f2)
print(f1 + f2)
print('--------------- sort_values --------------')
print(f1.sort_values(['b'], ascending=True)) # 升序
print(f1.sort_values(by='c', ascending=False)) # 降序
print('--------------- sort_index --------------')
print(f1.sort_index())
f1.sort_index(inplace=True)
print(f1)
print("================= DataFrame calc/total ===================================")
print(f1)
print(f1.mean()) # 均值
print("mean-a:", f1['a'].mean()) # 只统计数字 空/字符串不统计
print(f1.mean(axis = 1))
f1['mean'] = f1.mean(axis = 1, skipna=False) # skipna不忽略空值,可以用来判断有没有空值
print(f1)
# sum count(非空数量) min max median(中位数) std(标准差) var(方差) skew(偏度) kurt(峰度)
print(f.quantile(q=0.75)) # 分位数 q为中位数
# cumsum(累加) cumprod(累积) cummax(累积最大值) cummin(累积最小值) 
# unique(所有唯一值) values_count(统计不同值出现的次数)
print(f1.isin([0.5, 0.6])) # 判断是否在里边

print("================= DataFrame text ===================================")
fs = pd.DataFrame({'a': list("abcdefg"),
	'b': [np.nan,'asd','cvb','z','v','adf','k']})
print(fs)
print(fs['b'].str.count('a'))
print(fs['a'].str.upper())
# lower() len() startswith('a') ednswith('b')
# 去除空格 strip lstrip rstrip
# replace(' ', '', n=1) n:第几个
# split(',', expand=True).str[0] expand:

print("======================= ===================================")
# pandas 内存中连接操作，与关系型数据库非常相似
# merge() 参数：
# concat()
# duplicated()
# replace()
# groupby() 
	# first()
	# last()
	# sum()
	# mean() # 非NaN平均
	# median() # 非空算数中位数
	# count()
	# min()
	# std() # 标准差 
	# var() # 方差
	# prod() # 非空的积
	# agg() 


