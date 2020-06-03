

    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "% matplotlib inline\n",
    "# 导入模块\n",
    "\n",
    "import warnings\n",
    "warnings.filterwarnings('ignore') \n",
    "# 不发出警告"

    "# 数据分布的图表可视化 - 直方图\n",
    "\n",
    "r = np.random.RandomState(1)\n",
    "ar = r.randn(1000) * 100  # 创建一个正态分布数组\n",
    "\n",
    "plt.hist(ar,bins = 50)\n",
    "plt.grid()"

    "# 数据分布的图表可视化 - 箱型图\n",
    "\n",
    "plt.boxplot(ar,\n",
    "            vert = True,  # 是否垂直\n",
    "            whis = 1.5,  # IQR，默认1.5，也可以设置区间比如[5,95]，代表强制上下边缘为数据95%和5%位置\n",
    "            patch_artist = True,  # 上下四分位框内是否填充，True为填充\n",
    "            meanline = False,showmeans=True,  # 是否有均值线及其形状\n",
    "            showbox = True,  # 是否显示箱线\n",
    "            showcaps = True,  # 是否显示边缘线\n",
    "            showfliers = True,  # 是否显示异常值\n",
    "            notch = False,  # 中间箱体是否缺口\n",
    "            )\n",
    "plt.grid()"

    "# 计算分位数\n",
    "\n",
    "df = pd.DataFrame(ar,columns = ['value'])\n",
    "q25 = df['value'].quantile(0.25)\n",
    "q40 = df['value'].quantile(0.4)\n",
    "q75 = df['value'].quantile(0.75)\n",
    "print('df的25分位数为%.2f, 40分位数为%.2f, 75分位数为%.2f' % (q25,q40,q75))\n",
    "print('df的中位数为%.2f' % df['value'].median())\n",
    "print('-------')\n",
    "# pandas中为.quantile()\n",
    "\n",
    "a25 = np.percentile(ar,25)\n",
    "a40 = np.percentile(ar,40)\n",
    "a75 = np.percentile(ar,75)\n",
    "print('ar的25分位数为%.2f, 40分位数为%.2f, 75分位数为%.2f' % (a25,a40,a75))\n",
    "# numpy中为.percentile()"
    