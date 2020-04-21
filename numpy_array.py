import numpy as np

ar = np.array([[1,2,3,4,5,6],[6,5,4,3,2,1]])
print(ar)
print(ar.ndim) # 维度 秩rank
print(ar.shape) # 几行几列。。。。
print(ar.size) # 元素总个数 n行m列为n*m
print(ar.dtype) # 元素类型
print(ar.itemsize) # 字节大小
print(ar.data) # 

print("================= arange ===============")
print(np.arange(10))
print(np.arange(10.0))
print(np.arange(5,9))
print(np.arange(3.0, 7.0))
print(np.arange(10000))
print()

print("================= linspace ===============")
ar1 = np.linspace(2.0, 3.0, num=5)
ar2 = np.linspace(2.0, 3.0, num=5, endpoint=False)
ar3 = np.linspace(2.0, 3.0, num=5, retstep=True) # 记录步长
print(ar1, type(ar1))
print(ar2, type(ar2))
print(ar3, type(ar3))
print()


print("================= zeros ===============")
ar1 = np.zeros(5)
ar2 = np.zeros((5,5))
ar3 = np.zeros((2,2), dtype = np.int)
ar4 = np.zeros((3,3,3))
print(ar1, type(ar1))
print(ar2, type(ar2))
print(ar3, type(ar3))
print(ar4, type(ar4))
print()

print("================= zeros_like ===============")
ar1 = np.array([list(range(5)),list(range(5,10))])
ar2 = np.zeros_like(ar1)
print(ar1, type(ar1))
print(ar2, type(ar2))
print()

print("================= ones/ones_like ===============")
print("same like zeros")
print()

print("================= eye ===============")
print(np.eye(5)) # 对角线为1
print()

print("================= index/cut ===============")
ar1 = np.arange(16)
print(ar1)
print(ar1[3])
print(ar1[3:6])
print("---------------- reshape --------------")
ar1 = ar1.reshape(4,4)
print(ar1)
print(ar1[2][2])
print("------ cut ------")
print(ar1[1:3])
print(ar1[:3,2:])
print("------ boolean ------")
ar1 = np.arange(12).reshape(3,4)
i = np.array([True, False, True])
j = np.array([True, False, False, True])
print(ar1)
print(i)
print(ar1[i,:])
print(j)
print(ar1[:,j])
print(ar1[i,j])
print()

print("================= normal ===============")
# 标准正太分布
print(np.random.normal(size=(100)) )
print()

print("================= rand ===============")
# 均匀分布随机浮点数
print(np.random.rand(4) )
print(np.random.rand(2,3))
print()

print("================= randn ===============")
# 正太分布 不一定标准
print(np.random.randn(10))
print(np.random.randn(2,3))
print()

print("================= randint ===============")
# 随机整数
print(np.random.randint(10))
print(np.random.randint(2, size=5))
print(np.random.randint(2,6, size=5))
print(np.random.randint(2, size=(2,3)))
print(np.random.randint(2,6, (2,3)))
print()

print("================= RandomState ===============")
# 随机种子 生成的随机数不变
rng = np.random.RandomState(1) # 参数为随机序号 确定随机数
print(rng.randn(3,2))
print()