# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values #These are the features
y = dataset.iloc[:, 3].values #These are the results

#In the case of missing data, we can fill it in with the mean of the rest of the data.
#I presume that this is because taking the mean of something will not significantly
#affect the median, and will have no effect on the mean of the whole data set.
#removing the data point is disastrous, doing so could leave out extremely important
#information.
from sklearn.preprocessing import Imputer

np.set_printoptions(threshold = np.nan)
imputer = Imputer(missing_values="NaN", strategy="mean", axis=0)
imputer = imputer.fit(X[:, 1:3]) #upper bound is excluded
X[:, 1:3] = imputer.transform(X[:, 1:3])

#np.set_printoptions(threshold = np.nan)

#Since we have multiple types of labels in our dataset, and it would be bad to 
#have that appear in our machine learning model, we want to definitely change
#it to one-hot, this will ensure that we represent each label correctly as a #
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

#The reason this labelEncoder is bad is because it gives each label a presumed
#weight. This would be ideal if we can compare values that have a defined weight.
#Ex: Large (3) > Medium (2) > Small (1). Hence it makes the most sense to do Label Encoding.

#But we must do this step so that we can one hot encode.
labelEncoder_X = LabelEncoder()
X[:, 0] = labelEncoder_X.fit_transform(X[:, 0]) # NOTICE THIS IS BAD FOR THE CURRENT EXAMPLE

#However for this example it would be most ideal to instead use OneHotEncoder, because
#We can't compare the countries easily
oneHotEncoder = OneHotEncoder(categorical_features=[0])
X = oneHotEncoder.fit_transform(X).toarray()
  
#don't forget to do it for the purchased boolean col.
labelEncoder_y = LabelEncoder()
y = labelEncoder_y.fit_transform(y)


#Ideally we want to split our dataset into a training and a test set,
#this is because we don't want our model to learn the correlation of one set too
#well. If it does, then we'll have trouble, because then it won't be well adapted
#when given a new data set. For this, reason we split it into a training and test set.
#accuracy will be roughly the same between both sets
from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=0)


#Now we want to feature scale, the reason we do this is because if the features
#are on different scales, then obviously if one has a much larger range than another
#one of the features could be completely off.
#We can use two methods to scale the features, standardization and normalization.
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.fit_transform(X_test)








