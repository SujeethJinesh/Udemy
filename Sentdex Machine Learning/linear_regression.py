import pandas as pd
import quandl

df = quandl.get("WIKI/GOOGL") # importing dataset

# print(df.head())

df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']] # these are the columns of interest

df['High_Low_Percent_Difference'] = (df['Adj. High'] - df['Adj. Close'])/df['Adj. Close'] * 100 #high low percent difference
df['Percent_Change'] = (df['Adj. Close'] - df['Adj. Open'])/df['Adj. Open'] * 100 # percent change for the day

df = df[['Adj. Close', 'High_Low_Percent_Difference', 'Percent_Change', 'Adj. Volume']] # printing out new calculations

# print(df.head())
