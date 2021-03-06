#Description: This program detects if an individual has parkinson's disease.

#Import dependencies
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import classification_report
import seaborn as sns
from xgboost import XGBClassifier

from google.colab import files
uploaded = files.upload()

df = pd.read_csv('parkinsons.data')
df.head()

df.isnull().values.any()

df.shape

#Get the target counts
df['status'].value_counts()

percent_has_disease = 147/(147+48) * 100
percent_doesnot_have_disease = 48/(147+48) * 100

print(percent_has_disease)
print(percent_doesnot_have_disease)

#Visualize the count
sns.countplot(df['status'])

#Get the datatypes
df.dtypes

#Create the feature dataset
X = df.drop(['name'], 1)
X = np.array(X.drop(['status'], 1))

#Create the target dataset
y = np.array(df['status'])

#Split the data into 80% training and 20& testing datasets
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

#Transform the features data to be values between 0 to 1
sc = MinMaxScaler(feature_range=(0,1))
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

#Create the XGBClassifier
model = XGBClassifier().fit(x_train,y_train)

#Get the model predictions
predictions = model.predict(x_test)
print(predictions) 


print(y_test)

#Get the models accuracy, precision, recall and f1-score
print( classification_report(y_test, predictions))
