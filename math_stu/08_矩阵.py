
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "% matplotlib inline\n",
    "# 导入模块\n",
    "\n",
    "import warnings\n",
    "warnings.filterwarnings('ignore') \n",
    "# 不发出警告"

    "np.arange(50).reshape(10,5)\n",
    "# 构造一个10*5的矩阵"

    "np.eye(10)*10\n",
    "# 10阶方阵，当对角线值为1时为对角矩阵\n",
    "np.eye(5)"

    "a = np.arange(10)\n",
    "print(a)\n",
    "print(a.shape)\n",
    "# 行向量"

    "a = np.arange(10).reshape(10,1)\n",
    "print(a)\n",
    "print(a.shape)\n",
    "# 列向量"

    "2.2.2 矩阵的运算"

    "ar1 = np.arange(12).reshape(3,4)\n",
    "ar2 = np.arange(10,22).reshape(3,4)\n",
    "ar3 = np.ones((3,4))\n",
    "ar4 = np.ones((3,5))\n",
    "print(ar1)\n",
    "print(ar2)\n",
    "print(ar3)\n",
    "print(ar4)"

    "# 矩阵加法\n",
    "\n",
    "print(ar1+ar2)\n",
    "print(ar1+ar2+ar3)\n",
    "#print(ar1+ar4)\n",
    "# shape需要相同"

    "# 数与矩阵相乘\n",
    "\n",
    "ar1 * 10"

    "# 数组与矩阵相乘\n",
    "\n",
    "print(ar1*ar2) \n",
    "#print(ar1*ar4)\n",
    "print('------')\n",
    "# 数组相乘 → numpy里面两个shape相同的数组可以直接相乘，对应位置的值的乘积为结果\n",
    "# 如果shape不同，则报错\n",
    "\n",
    "a1 = np.array([2,3,4])\n",
    "b1 = np.array([5,6,7]).reshape(3,1)  # 转换为列向量\n",
    "c1 = np.dot(a1,b1)\n",
    "print(a1.shape,b1.shape,c1.shape)\n",
    "print(c1,type(c1))\n",
    "\n",
    "a2 = np.array([\n",
    "        [1,2,3],\n",
    "        [2,3,4]\n",
    "    ])\n",
    "b2 = np.array([\n",
    "        [4,4],\n",
    "        [5,5],\n",
    "        [6,6]\n",
    "    ])\n",
    "c2 = np.dot(a2,b2)\n",
    "print(a2.shape,b2.shape,c2.shape)\n",
    "print(c2)\n",
    "# 矩阵乘法，需要保证第一个矩阵的列数（column）和第二个矩阵的行数（row）相同\n",
    "# 设 A = (aij) 是一个m×s 矩阵, B = (bij)是一个s×n矩阵，那么规定矩阵A与矩阵B的乘积是一个m×n的矩阵\n",
    "# 矩阵相乘结果仍为矩阵\n",
    "# numpy中用.dop()来计算矩阵乘法"

    "# 矩阵乘法：A*B 与 B*A\n",
    "\n",
    "a3 = np.array([\n",
    "        [-2,4],\n",
    "        [1,-2]\n",
    "    ])\n",
    "b3 = np.array([\n",
    "        [2,4],\n",
    "        [-3,-6]\n",
    "    ])\n",
    "print(np.dot(a3,b3))\n",
    "print(np.dot(b3,a3))"

    "# 矩阵的转置\n",
    "\n",
    "A = np.array([\n",
    "        [2,0,-1],\n",
    "        [1,3,2]\n",
    "    ])\n",
    "B = np.array([\n",
    "        [1,7,-1],\n",
    "        [4,2,3],\n",
    "        [2,0,1]\n",
    "    ])\n",
    "np.dot(A,B).T"

    "2.2.3 逆矩阵\n",
    "* 设A是数域上的一个n阶矩阵，若在相同数域上存在另一个n阶矩阵B，使得： AB=BA=E ，则我们称B是A的逆矩阵，而A则被称为可逆矩阵。注：E为单位矩阵 → 单位矩阵值为1\n",
    "* 唯一性：若矩阵A是可逆的，则A的逆矩阵是唯一的\n",
    "* A的逆矩阵的逆矩阵还是A。记作（A-1）-1=A\n",
    "* 可逆矩阵A的转置矩阵AT也可逆，并且（AT）-1=（A-1）T (转置的逆等于逆的转置）\n",
    "* 两个可逆矩阵的乘积依然可逆"

    "# 创建A矩阵\n",
    "\n",
    "A = np.array([\n",
    "        [1,2,3],\n",
    "        [2,2,1],\n",
    "        [3,4,3]\n",
    "    ])\n",
    "print(A)\n",
    "print(np.linalg.det(A))"

    "# numpy求逆矩阵B → np.linalg.inv()\n",
    "\n",
    "B = np.linalg.inv(A)\n",
    "print(B)\n",
    "print(np.linalg.det(B))"

    "# A*B = E，单位矩阵\n",
    "\n",
    "E = np.dot(A,B)\n",
    "print(E)\n",
    "print(np.linalg.det(E))\n",
    "#np.eye(3)"

    "# 伴随矩阵\n",
    "\n",
    "A_bs = B*np.linalg.det(A)\n",
    "print(A_bs)\n",
    "print(np.linalg.det(A_bs))"

    "# 练习1\n",
    "\n",
    "a = np.array([\n",
    "        [4,1,2,4],\n",
    "        [1,2,0,2],\n",
    "        [1,0,2,0],\n",
    "        [0,1,1,0]\n",
    "    ])\n",
    "\n",
    "print(np.linalg.inv(a))\n",
    "np.linalg.det(a)"

    "# 练习2\n",
    "\n",
    "a = np.array([\n",
    "        [1,1,1],\n",
    "        [1,2,4],\n",
    "        [1,3,9]\n",
    "    ])\n",
    "a1 = np.array([\n",
    "        [2,1,1],\n",
    "        [3,2,4],\n",
    "        [5,3,9]\n",
    "    ])\n",
    "a2 = np.array([\n",
    "        [1,2,1],\n",
    "        [1,3,4],\n",
    "        [1,5,9]\n",
    "    ])\n",
    "a3 = np.array([\n",
    "        [1,1,2],\n",
    "        [1,2,3],\n",
    "        [1,3,5]\n",
    "    ])\n",
    "\n",
    "x1 = np.linalg.det(a1)/np.linalg.det(a)\n",
    "x2 = np.linalg.det(a2)/np.linalg.det(a)\n",
    "x3 = np.linalg.det(a3)/np.linalg.det(a)\n",
    "\n",
    "print('该方程的三个根为：x1=%.2f, x2=%.2f, x3=%.2f' % (x1,x2,x3))"
    