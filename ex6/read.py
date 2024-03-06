import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import re

def filter_location(string):
    result =  re.findall("\,\ [A-Z]{2}$",string)

data = pd.read_excel("final_project.ods", engine="odf")


target = "career_level"
x = data.drop(target, axis=1)
y = data[target]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=63, stratify=y)

print(data["career_level"].unique())

vectorizer = TfidfVectorizer(stop_words="english")
# result = vectorizer.fit_transform((x_train["title"]))
# print(vectorizer.vocabulary_)
# print(len(vectorizer.vocabulary_))
# print(result.shape)

encoder = OneHotEncoder()
result = encoder.fit_transform(x_train[["location"]])
print(result.shape)

