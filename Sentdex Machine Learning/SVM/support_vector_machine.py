import numpy as np
from sklearn import preprocessing, cross_validation, neighbors, svm
import pandas as pd

# Read in CSV
df = pd.read_csv('breast-cancer-wisconsin.data.txt')

# Replace ? with -99999 so we have proper data
df.replace('?', -99999, inplace=True)

# Want to get rid of unecessary data. The id column has nothing to do with cancer
df.drop(['id'], 1, inplace=True)

# Getting our sample and validation sets ready
X = np.array(df.drop(['class'],1))
y = np.array(df['class'])

# splitting training and testing data
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y,test_size=0.2)

# Importing our classifier
classifier = svm.SVC()

# Fitting the classifer
classifier.fit(X_train, y_train)

accuracy = classifier.score(X_test, y_test)
print(accuracy)


example_measures = np.array([[4,2,1,1,1,2,3,2,1],[4,2,1,3,1,4,3,2,1]])
example_measures = example_measures.reshape(len(example_measures),-1)

prediction = classifier.predict(example_measures)
print(prediction)
