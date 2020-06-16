# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 14:30:14 2020

@author: chang
"""


import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv('freq_counted_data.csv')
unrate['YEAR'] = pd.to_datetime(unrate['YEAR'])

# 

print(unrate.head(22))
first_twenty = unrate[1:20] #获取前20行数据

for row in unrate:
    topic.append(row[1], column[3:22])
plt.pie(topics, label=topic)
plt.axis('equal')
plt.show()
