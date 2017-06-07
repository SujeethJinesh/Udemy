import pandas as pd
import quandl, math, datetime
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt 
from matplotlib import style
import pickle

style.use('ggplot') # make the plot look actually good

df = quandl.get("WIKI/GOOG") # importing dataset of stock you wish to use

# print(df.head())

df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']] # these are the columns of interest

df['High_Low_Percent_Difference'] = (df['Adj. High'] - df['Adj. Close'])/df['Adj. Close'] * 100 #high low percent difference
df['Percent_Change'] = (df['Adj. Close'] - df['Adj. Open'])/df['Adj. Open'] * 100 # percent change for the day

df = df[['Adj. Close', 'High_Low_Percent_Difference', 'Percent_Change', 'Adj. Volume']] # printing out new calculations

# print(df.head())

forecast_col = 'Adj. Close' # label for what we want to predict

# df.fillna(-9999, inplace=True) # replacing the nans with outlier data, might want to consider the avg of the column as well.
df.apply(lambda x: x.fillna(x.mean()),axis=0) #this might help with replacing with the avg --> looks like it has very little effect on pred

forecast_out = int(math.ceil(0.01*len(df))) # want to predict a data point 1% ahead. i.e. if you have 10 days of data, you can predict 1 day in advance

df['label'] = df[forecast_col].shift(forecast_out) # Shifting out how far we wanna go?
# print(df.head())

X = np.array(df.drop(['label'], 1)) # features
X = preprocessing.scale(X) # normalizes the features
X_lately = X[-forecast_out:]
X = X[:-forecast_out]

df.dropna(inplace=True)
y = np.array(df['label'])

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2) # Splitting into training(80%) and testing(20%)

# classifier = LinearRegression() # classifier we are choosing
# classifier = svm.SVR() # if you wanna switch the classifier, you can do this.
# classifier = svm.SVR(kernel='poly') # can switch around the type as well
classifier = svm.SVR(kernel='rbf', C=1e3, gamma=0.1) # Seems like a decent fit, might wanna have multiple ones.

classifier.fit(X_train, y_train) # fitting our classifier to the data

##### Following is to save trained classifier

with open('linearregression.pickle', 'wb') as f:
    pickle.dump(classifier, f)

pickle_in = open('linearregression.pickle', 'rb')
classifier = pickle.load(pickle_in)

#####

accuracy = classifier.score(X_test, y_test) # scoring our data against the testing data

forecast_set = classifier.predict(X_lately)

# print(forecast_set, accuracy, forecast_out)
df['Forecast'] = np.nan

last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]

print(df.tail())

df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.title("GOOG")
plt.show()
