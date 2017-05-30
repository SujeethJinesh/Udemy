import pandas as pd
import quandl, math
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression

df = quandl.get("WIKI/GOOGL") # importing dataset

# print(df.head())

df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']] # these are the columns of interest

df['High_Low_Percent_Difference'] = (df['Adj. High'] - df['Adj. Close'])/df['Adj. Close'] * 100 #high low percent difference
df['Percent_Change'] = (df['Adj. Close'] - df['Adj. Open'])/df['Adj. Open'] * 100 # percent change for the day

df = df[['Adj. Close', 'High_Low_Percent_Difference', 'Percent_Change', 'Adj. Volume']] # printing out new calculations

# print(df.head())

forecast_col = 'Adj. Close' # label for what we want to predict

df.fillna(-9999, inplace=True) # replacing the nans with outlier data, might want to consider the avg of the column as well.

forecast_out = int(math.ceil(0.01*len(df))) # want to predict a data point 10% ahead. i.e. if you have 10 days of data, you can predict 1 day in advance

df['label'] = df[forecast_col].shift(-forecast_out) # ??
df.dropna(inplace=True)
# print(df.head())

X = np.array(df.drop(['label'], 1)) # features
y = np.array(df['label']) #

X = preprocessing.scale(X) # normalizes the features
y = np.array(df['label'])

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2) # Splitting into training(80%) and testing(20%)

classifier = LinearRegression() # classifier we are choosing

classifier.fit(X_train, y_train) # fitting our classifier to the data
accuracy = classifier.score(X_test, y_test) # scoring our data against the testing data

print(accuracy)
