import numpy as np

print("=============================== basic =========================")
ar1 = np.arange(20)
print("reshape\n", ar1.reshape(4,5)) # 不修改原数组
print("reshape.T\n", ar1.reshape(4,5).T) # 转置
print("old",ar1)
ar2 = ar1.copy()
print("copy", ar2)
ar1.resize(5,5) # 修改原数组
print("resize5-5\n", ar1)
ar1.resize(3,4) 
print("resize3-4\n", ar1)
print("astype-float", ar2.astype(np.float))

print("=============================== hstack =========================")
# 横向相加
a = np.arange(5)
b = np.arange(5,9)
ar1 = np.hstack((a,b))
print(a, a.shape)
print(b, b.shape)
print(ar1, ar1.shape)
a = np.array([[1], [2], [3]])
b = np.array([[4], [5], [6]])
ar1 = np.hstack((a,b))
print(a, a.shape)
print(b, b.shape)
print(ar1, ar1.shape)

print("=============================== vstack =========================")
# 纵向相加
a = np.arange(5)
b = np.arange(5,10)
ar1 = np.vstack((a,b))
print(a, a.shape)
print(b, b.shape)
print(ar1, ar1.shape)
a = np.array([[1], [2], [3]])
b = np.array([[4], [5], [6], [7]])
ar1 = np.vstack((a,b))
print(a, a.shape)
print(b, b.shape)
print(ar1, ar1.shape)

print("=============================== stack =========================")
a = np.arange(5)
b = np.arange(5,10)
print("a:", a, a.shape)
print("b:", b, b.shape)
ar1 = np.stack((a,b))
print("stack:\n", ar1, ar1.shape)
ar1 = np.stack((a,b), axis = 1)
print("stack-a1:\n", ar1, ar1.shape)

print("=============================== hsplit =========================")
# 拆分
a = np.arange(16).reshape(4,4)
print("a:\n", a, a.shape)
ar = np.hsplit(a, 2);
print("ar-hsplit:\n", ar)
ar = np.vsplit(a, 2);
print("ar-vsplit:\n", ar)


print("=============================== +-*/ =========================")
# 运算
a = np.arange(16).reshape(4,4)
print("a:\n", a)
print("a+10:\n", a+10)
print("a-9:\n", a-9)
print("a*3:\n", a*3)
print("a/2:\n", a/2)
print("a-mean:", a.mean())
print("a-max:", a.max())
print("a-min:", a.min())
print("a-std:", a.std())
print("a-var:", a.var())
print("a-sum:", a.sum(), np.sum(a, axis = 0)) # 0:列 1:行
print("sort:",np.sort(np.array([1,2,5,6,8,4,2,6,3])))