# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 22:37:10 2018

@author: Suman
"""

from trendTheta import trendTheta
from Mean_reversion import mr
import pandas as pd
import matplotlib.pyplot as plt
from Compute_KPI_OutputClass import Output
import numpy as np

weights = [0.9577,0.0423]


nf = pd.read_csv('NIFTY.csv',index_col=0,header=0)
nf_stocks = pd.read_csv('dataNF50.csv',index_col=0,header=0)
nf_stocks.dropna(inplace=True)
nf_stocks.index = nf.index

ret1 = trendTheta()
ret2 = mr(nf_stocks,nf)
#ret1.index = pd.to_datetime(ret1.index)
#x = Output(ret1)


#x = Output(ret2)
#print(x.generate_output())

df = pd.DataFrame()
df["trendTheta"] = ret1[:len(ret2)-len(ret1)]
df["meanRevertion"] = list(ret2)
df ["Portfolio"] = np.dot(weights,[df.trendTheta,df.meanRevertion])
x = Output(df)
print(x.generate_output())

df.cumsum().plot(figsize=(12,6))
plt.ylabel('Cumulative Returns')  
plt.legend()
plt.grid()
plt.show()
