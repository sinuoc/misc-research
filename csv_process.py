import csv
import math
import numpy as np 
import sys, os
from matpltlib import pyplot

listage = []
listnum = []

with open('dominant_topics_processed.csv','r',encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)

    for row in reader:
        listage.append(row[0])
        listnum.append(row[4104])
    
x = listage
y = listnum

pyplot.plot(x, y,)
pyplot.xticks([2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020], ["2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020"])
pyplot.xlabel("Year")
pyplot.show