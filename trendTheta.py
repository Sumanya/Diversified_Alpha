# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 20:01:29 2018

@author: Suman
"""

#importing modules
import pandas as pd
import nsepy as ny
from datetime import date
import matplotlib.pyplot as plt
from nsepy import derivatives
import talib as ta
import datetime as dt
from Compute_KPI_OutputClass import Output


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
    nf = ny.get_history(symbol= "NIFTY",start=start,end=expry[-1],index = True)
    
    
    #Downloading Closing prices and Pnl Calculation
    p = nf.index[0] 
    pnl = []  

    for x in range(len(expry)):
        while p not in nf.index:
            p -= dt.timedelta(1)
            
        strk = int(int(nf[nf.index == p].Close)*0.0097)*100 #Chosing strike below 97% of spot
        #Collecting Put EOD data
        put = ny.get_history(symbol="NIFTY",start=p,end=expry[x],index = True,option_type="PE",strike_price=strk,expiry_date= expry[x])
        put["prevClose"] = put["Close"].shift(1)
        put["diff"] = put.prevClose - put.Close
        pnl.extend(list(put["diff"].dropna()))
        pnl[-1] -= 4   #Cost during entering and rolling over
        p = expry[x]
        
#    print(len(pnl))
    
    #Using the long term trends to short and exit from mkt during mkt fall(below 10EMA)
    m = 20
    df= pd.DataFrame()
    df["Close"] = nf.Close[1:len(pnl)+1]
#    print(len(df))
    df["shortPut"] = pnl[:len(df)]        
    df["EMA"] = ta.EMA(df.Close,timeperiod=m)
    df =  df.dropna()
    df["Long"] = df.apply(lambda x : 1 if x['EMA'] < x['Close'] else 0, axis=1)
    df["Change"] = df['Long'] != df['Long'].shift(1) 
    df = df.applymap(lambda x: 1 if x == True else x)
    df = df.applymap(lambda x: 0 if x== False else x)
    df["Pnl"] = df["Long"]*df["shortPut"] - df["Change"]*4 #Cost while exiting and re-entering
    df.loc[df.index[0],"Pnl"] += 1500   
    df["Result"] = df["Pnl"].cumsum()
#    plt.plot(df["Result"].pct_change())
    
    return df["Result"].pct_change().dropna()