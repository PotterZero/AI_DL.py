import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report


data = pd.read_csv("diabetes.csv")

target = "Outcome"
x = data.drop(target, axis=1)
y = data[target]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=2024)

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

param_grid = {
    "n_estimators": [50, 100, 200],
    "criterion": ["gini", "entropy", "log_loss"]
}

grid_search = GridSearchCV(RandomForestClassifier(), param_grid=param_grid, verbose=1, cv=4, scoring="recall")
grid_search.fit(x_train, y_train)
y_predict = grid_search.predict(x_test)
print(grid_search.best_params_)
print(grid_search.best_score_)
print(classification_report(y_test,y_predict))









