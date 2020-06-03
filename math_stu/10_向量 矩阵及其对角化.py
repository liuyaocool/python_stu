
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "% matplotlib inline\n",
    "# 导入模块\n",
    "\n",
    "import warnings\n",
    "warnings.filterwarnings('ignore') \n",
    "# 不发出警告"

    "2.4.3 向量的性质\n",
    "* np.linalg.eigvals() → 计算矩阵的特征值\n",
    "* np.linalg.eig() → 返回包含特征值和对应特征向量的元组"

    "# 例子1\n",
    "\n",
    "a = np.array([\n",
    "        [3,-1],\n",
    "        [-1,3]\n",
    "    ])\n",
    "print(np.linalg.eigvals(a))\n",
    "print(np.linalg.eig(a))"

    "# 例子2\n",
    "\n",
    "a = np.array([\n",
    "        [-1,1,0],\n",
    "        [-4,3,0],\n",
    "        [1,0,2]\n",
    "    ])\n",
    "print(np.linalg.eigvals(a))\n",
    "print(np.linalg.eig(a))"

    "2.4.4 矩阵的对角化\n",
    "* np.diag() → 对角化"

    "a = np.array([\n",
    "        [-2,1,1],\n",
    "        [0,2,0],\n",
    "        [-4,1,3]\n",
    "    ])\n",
    "print(np.linalg.eigvals(a)) \n",
    "# 得到特征值\n",
    "np.diag(np.linalg.eigvals(a))\n",
    "# 得到对角化矩阵"
    