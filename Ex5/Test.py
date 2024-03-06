import pandas as pd
from sklearn.model_selection import train_test_split  # dùng để chia data
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline    # dùng để nối bước
from sklearn.impute import SimpleImputer # dùng để điền vào các null

data = pd.read_csv("StudentScore.xls")

target = "math score"

x = data.drop(target, axis=1)
y = data[target]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=2024)

num_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

result = num_transformer.fit_transform(data[["math score", "writing score"]])

for i,j in zip(data[["math score","writing score"]].values, result):
    print("Before: {}. After: {}".format(i, j))














