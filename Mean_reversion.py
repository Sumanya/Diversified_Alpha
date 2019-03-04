# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 20:04:09 2018

@author: Suman
"""

import pandas as pd
import statsmodels.api as sm
import statsmodels.tsa.stattools as ts
import matplotlib.pyplot as plt
from Compute_KPI_OutputClass import Output

def hedge_ratio(y,x):
    # Ordinary Least Squares regression to find hedge ratio    
    if x.empty:
        return [0]    
    model = sm.OLS(y, x)
    return model.fit() 
    #print 'Hedge Ratio =', model.params[0]    
    
def cadf(y,x):            
    # Hedge Ratio
    model = hedge_ratio(y,x)
    # Create Portfolio       
    portfolio = y - model.params[0] * x     
    # Perform stationarity test on portfolio 
    try:
        return ts.adfuller(portfolio)    
    except:        
        return [0]        
def mr(x,y):
    nf_components = x
    nf = y
    
    coint_stat=pd.Series(index=nf_components.columns)
    N = 200
    for s in nf_components.columns:    
        results = cadf(nf.iloc[:N]['NIFTY'], nf_components.iloc[:N][s])    
        coint_stat[s] = results[0]
    
    coint_stat.sort_values(inplace=True)
    stocks_to_trade = coint_stat.index
    model = hedge_ratio(nf.iloc[:N]['NIFTY'], nf_components.iloc[:N][stocks_to_trade])
    
    nf_components = nf_components[N+152:]
    nf = nf[N+152:]
    basket_MV = pd.Series(index=nf_components.index, data=0.0)
    
    for s in stocks_to_trade:            
        basket_MV += model.params[s]*nf_components[s]
        
    basket= nf["NIFTY"] - basket_MV
    basket["rets"] = basket.pct_change().dropna()

    return (basket["rets"])