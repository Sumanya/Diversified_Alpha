# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 20:01:29 2018

@author: Suman
"""

#importing modules
import pandas as pd
from datetime import date
import matplotlib.pyplot as plt
import datetime as dt


def trendTheta():
    #Date range and collecting derivatives expiry dates
    start = date(2015,1,1)
    end = date(2018,11,27)
    expry = []
    for y in range(start.year,end.year+1):
        for m in range(1,13):
            expry.append(derivatives.get_expiry_date(y,m,index=True))
    expry[38] = date(2018, 3, 28) # replacing a change in expiry by NSE
    
    
    #Importing spot data used to calculate strike prices
    nf = data    
    
    #Downloading Closing prices and Pnl Calculation
    p = nf.index[0] 
    pnl = []  

    for x in range(len(expry)):
        while p not in nf.index:
            p -= dt.timedelta(1)
            
        df = Pnl(data)
    return df["Result"].pct_change().dropna()
