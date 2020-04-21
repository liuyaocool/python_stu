# ctrl b 解释运行
print("hello")
print(type(10))

#运算 同java
#比较 同java

a = 10
print(a//7) #除法取整
print(a**2) #a的2次方
print(a**3) #a的3次方
print(a%3) #取余数

print(True or False)
print(True and False)
print(not False)
print(False == 0)
print(True == 1)
print(True*10)

#字符串 单引号 双引号 同java
#三引号
str1 = '''aaa
bbb
ccc'''
print(str1)
print('aaa\nbbb\nccc') #同上
print(r'aaa\nbbb\nccc')
print('this is', 1, 'study')
print("a" + "b")
print("A" * 6)
print("g" in "adsfasdfgghrthg")
print("g" not in "adsfasdfgghrthg")

print(len('1234567'))
print(str(123213), str(12.45))
print(int("123213"), float("12.45"))
print(eval("12-6")) # 执行字符串中的内容
print("heool".replace("h", "a"))
print("adsf,adfr,qtr".split(","))

var1 = 20
var2 = 12.1212434
var3 = "小明"
# print('我有%i块钱', % var1)
# print("我得了%f分", % var2)
# print("我得了%.2f分", % var2)
# print("他叫%s吗", % var3)
# print("他叫%s,考了%f分", % (var3,var2))

#列表 可变
list1 = [1,2,3,4,'a', 'b', 'c', [1,2,3]]
print(list1[3])
print(list1[-2])
print(list1[2:4])
print(list1[2:4:3]) #3为步长
# len(list1)
# max(list1)
# min(list1)
# sum(list1)
list1.index(2)
list1.count(2) # 计算2出现的次数
list1.append('w')
list1.extend('a')
list1.insert(2, 'z')
list2 = list1.copy()
# list2.sort()
# list2.sort(reverse=True) #反向排序
#元组 不可变数列  
tup1 = (1,2,3,4,'a','b',(1,'b'))
# 同上
#字典 同js
dic1 = {"name": "小明", "age": 123}
print(dic1["name"])
print(id(dic1))
dic2 = dic1.copy()
del dic1 # 删除变量
# print(dic1["name"])
print(dic2.keys())


# 使用缩进来确定代码块
if 1 < 2:
	print(1)
elif 2 < 3:
	print(2)
else:
	print(3)

for i in list1:
	print(i)

for i in list1:
	# break continue
	pass #空语句 保证代码完整型

# while else 语句
while 3 < 2:
	print("aaa")
else:
	print("bbb")

#函数 j为可变参数
def f1(n, m, *j):
	listf = []
	for i in range(m):
		listf.append(n)
	print(j)
	global g1 # 定义为全局
	g1 = "全局变量"
	return listf

f1(1, 5, 'a', 'b')

import math
print(math.pi)
# help[math]

#导入自己的模块
import model as md
print(md.f2(12, 34))

import sys
sys.path.append("C:/Users/liuyao/Desktop/python/model")
import m1
print(m1.f3(12, 34))

# 单独导入方法
from m2 import f4,f5
print(f4(12,34))
print(f5(12,34))
# print(f6(12,34))