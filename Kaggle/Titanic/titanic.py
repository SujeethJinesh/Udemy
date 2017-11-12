#imports
import pandas as pd
import numpy as np
from sklearn import neighbors

#read in data, probably wanna use pandas
df_train = pd.read_csv('train.csv')
df_test = pd.read_csv('test.csv')

#drop unnecessary columns that don't effect survival rate
df_train.drop(['PassengerId', 'Name', 'Ticket', 'Parch', 'Cabin'], 1, inplace=True)
result = df_test['PassengerId'].to_frame() #make sure it's a dataframe and not a series
df_test.drop(['PassengerId', 'Name', 'Ticket', 'Parch', 'Cabin'], 1, inplace=True)

#one hot encode categorical values (m/f)
df_train = pd.get_dummies(df_train)
df_test = pd.get_dummies(df_test)

#fill nans with mean
df_train = df_train.fillna(df_train.mean())
df_test = df_test.fillna(df_test.mean())

#checking what the cleaned data looks like
np.savetxt(r'cleaned_data.txt', df_train.values, fmt='%d')

# sample and validation sets
X_train = np.array(df_train.drop(['Survived'],1)) #removing Survived col cause that's what we're testing.
y_train = np.array(df_train['Survived'])

#select classifier
classifier = neighbors.KNeighborsClassifier()

#fit data
classifier.fit(X_train, y_train)
prediction = classifier.predict(df_test)

#assign survived col to prediction
result['Survived'] = prediction

#feed output into csv
result.to_csv('gender_submission.csv', index=False)
