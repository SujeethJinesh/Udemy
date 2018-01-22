import pandas as pd
import quandl, math, datetime

import numpy as np
from sklearn import preprocessing, svm, model_selection
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')


df = quandl.get('WIKI/GOOGL')  # retrieves pandas data frame for certain ticker from quandl
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]  # selecting the cols we want

# The reason we're doing the following two lines is because we don't want to feed data that is too related to the
#  parameters that already exist. Hence we want to distill it into one feature for multi features that are too similar
# or could be described with 1 feature
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0  # high low percent
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0  # percent change for the day

df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

forecast_col = 'Adj. Close'  # to make the code extensible essentially
df.fillna(-99999, inplace=True)  # this is to fill in any data that doesn't exist, and this

forecast_out = int(math.ceil(0.01 * len(df)))  # this is how many days out we are trying to predict. in this case, 1%

# this is the label column
df['label'] = df[forecast_col].shift(-forecast_out)

X = np.array(df.drop(['label'], 1))  # X is all of our features
X = preprocessing.scale(X)  # scale our features
X = X[:-forecast_out]
X_lately = X[-forecast_out:]

df.dropna(inplace=True)
y = np.array(df['label'])  # our y values

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y,
                                                                    test_size=0.2)  # produces good shuffled train and test sets

classifier = LinearRegression(n_jobs=-1)  # you can replace the algorithm you want here
# classifier = svm.SVR(kernel='poly')
classifier.fit(X_train, y_train)  # does the prediction (training)

accuracy = classifier.score(X_test, y_test)  # (test)

# print(accuracy)

# predicting future values
forecast_set = classifier.predict(X_lately)

print(forecast_set, accuracy, forecast_out)

df['Forecast'] = np.nan
last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns) - 1)] + [i]

df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
