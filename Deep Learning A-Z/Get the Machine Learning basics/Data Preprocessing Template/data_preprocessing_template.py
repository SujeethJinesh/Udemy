# Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

##since we have missing data, we want to replace it with the avg for the row
#from sklearn.preprocessing import Imputer
#imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
#imputer.fit(X[:, 1:3]) #upper bound is excluded
#X[:, 1:3] = imputer.transform(X[:, 1:3])
#
##since some of the data is categorical (country name, yes/no) we need to encode that
#from sklearn.preprocessing import LabelEncoder, OneHotEncoder
#labelencoder_X = LabelEncoder()
#X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
##### Problem arises however if the model thinks that the returned values have relations
##### Ie, France > germany > spain, etc. prevent the model from thinking this by onehot
#
##### OneHot essentially splits the X vals into separate columns and puts a 1 if it's the cat
##### else it'll put a 0.
#onehotencoder = OneHotEncoder(categorical_features=[0])
#X = onehotencoder.fit_transform(X).toarray()
#
##### only need a label encoder for the dependent variable
#labelencoder_y = LabelEncoder()
#y = labelencoder_y.fit_transform(y)

### We want to split the data set into a training set, and a test set
### this is to ensure that the model doesn't find too strong of a correlation with the test
from sklearn.cross_validation import train_test_split, model_selection
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#Finally, we want to feature scale, this is to ensure that the scales of the inputs are comparable
#otherwise one of the features could have no effect (ex: age vs income scale).
#Can do standardization or normalization
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
