# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import csv
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


df = pd.read_csv(r'/Users/lilyngo/Downloads/BTC_USD_2020-04-19_2021-04-18-CoinDesk.csv',header=0,index_col=1,parse_dates=[0]) # rename to your path
df.plot(y=['Closing Price (USD)','24h Open (USD)','24h High (USD)','24h Low (USD)'])
plt.show()


data = pd.read_csv(r'/Users/lilyngo/Downloads/BTC_USD_2020-04-19_2021-04-18-CoinDesk.csv') # rename to your path
x = data['Closing Price (USD)']
y = data['24h High (USD)']

print(np.corrcoef(x, y))

plt.scatter(x, y)
plt.title('A plot to show the correlation ')
plt.xlabel('Closing Price (USD)')
plt.ylabel('24h High (USD)')
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), color='yellow')
plt.show()

