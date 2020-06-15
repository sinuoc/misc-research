import csv
import math
import numpy as np 
import sys, os
import pandas as pd
import seaborn as sns
from matpltlib import pyplot

# 分类
data=pd.DataFrame(columns=['Dominant_Topic','Publication_Year'], index=['1','2','3','4','5','6','7','8','9','']

## 注释掉的是旧代码

# listage = []
# listnum = []


# with open('dominant_topics_processed.csv','r',encoding='utf-8') as f:
    # reader = csv.reader(f)
    # header = next(reader)

    # for row in reader:
        # listage.append(row[0])
        # listnum.append(row[4104])
    
# x = listage
# y = listnum

#pyplot.plot(x, y,)
#pyplot.xticks([2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020], ["2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020"])
#pyplot.xlabel("Year")
#pyplot.show

plt.rcParams['figure.figsize'] = (8.0, 6.0)