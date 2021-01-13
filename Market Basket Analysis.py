# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 23:03:42 2020

@author: USER
"""

# import library 
import pandas as pd 
import numpy as np 


# import data 
df = pd.read_csv('data/market_basket.csv')


# preprocessing 
transaksi = []
for i in range(0, len(df)):
    transaksi.append([str(item) for item in df.values[i,:] if str(item) != 'nan'])


# training apriori 
from apyori import apriori 
asosiasi = apriori(transaksi, min_support=0.01, min_confidence=0.3, max_length=2, min_lift=1)


# hasil asosiasi 
hasil = list(asosiasi)
analisis_hasil = []
for i in range(0, len(hasil)):
    analisis_hasil.append('RULE:\t{}\nSUPP:\t{}\nCONF:\t{}\nLIFT:\t{}\n'.format(list(hasil[i][0]), str(hasil[i][1]), str(hasil[i][2][0][2]), str(hasil[i][2][0][3])))
