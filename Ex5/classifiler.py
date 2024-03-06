import pandas as pd
from ydata_profiling import ProfileReport
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

import matplotlib as plt

data = pd.read_csv("diabetes.csv")

#   print(data.info())
#   stat = data.describe()

#   pro = ProfileReport(data, title ="Report",explorative = True )
#   pro.to_file("diabetes_report.html")

target = "Outcome"
x = data.drop(target, axis=1)
y = data[target]

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state= 63)
#x_train, x_val, y_train, y_val = train_test_split(x,y, test_size=0.75)

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

clf = SVC()
clf.fit(x_train, y_train)
y_predict = clf.predict(x_test)
print(y_predict.shape)
print(y_test.shape)

#   for i, j in zip(y_predict,y_test):
#       print("Pre vl: {}. Act vl: {}".format(i,j))

print(classification_report(y_test,y_predict))