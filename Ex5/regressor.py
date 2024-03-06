import pandas as pd
from ydata_profiling import ProfileReport
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder

data = pd.read_csv("StudentScore.xls")
 
target = "math score"
x = data.drop(target, axis=1)
y = data[target]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=2024)

num_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

education_levels = ["master's degree", "bachelor's degree", "associate's degree", 'some college',
                    'high school', 'some high school']
gender_values = x_train["gender"].unique()
lunch_values = ["standard", "free/reduced"]
test_prep_values = x_train["test preparation course"].unique()
ord_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OrdinalEncoder(categories=[education_levels, gender_values, lunch_values, test_prep_values]))
])

nom_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder())
])

result = ord_transformer.fit_transform(x_train[["parental level of education", "gender", "lunch", "test preparation course"]])
for i, j in zip(x_train[["parental level of education", "gender", "lunch", "test preparation course"]].values, result):
    print("Before: {}. After: {}".format(i, j))