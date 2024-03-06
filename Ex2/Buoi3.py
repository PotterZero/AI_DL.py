import gensim.downloader as api
import numpy as np

# 25, 50, 100 or 200. Số càng lớn thì càng chính xác, nhưng chạy càng lâu các bạn nhé
model = api.load("glove-twitter-200")
word = "beautiful"
print(model[word])

print("1----------")
result = model.most_similar(word, topn=10)
print(result)

print("2----------")
result = model.most_similar(positive=["january", "february"], topn=10)
print(result)

print("3----------")
result = model.similarity("man", "woman")
print(result)

print("4----------")
result = model.most_similar(positive=["woman", "king"], negative=["man"], topn=1)
print(result)

print("5----------")
result = model.most_similar(positive=["berlin", "vietnam"], negative=["hanoi"], topn=1)
print(result)

print("6----------")
result = model.similarity("marriage", "happiness")
print(result)

print(" Calculate ")
#TODO: Calculate cosine simialrity by 2 ways
a = model["man"]
b = model["woman"]
result = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
print(result)