import numpy as np
import pandas as pd
import os

os.chdir('C:/Users/liuyao/Desktop/python/test')
d1 = pd.read_table('tb1.txt', delimiter=',',header=0,index_col=1)
print(d1)

# read_csv('', encoding='utf-8')
# read_excel('', sheet_name='')  or sheet_name=1,header=0,index_col=1