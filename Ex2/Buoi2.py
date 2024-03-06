print("===================Ex 1=========================")
import numpy as np
x = np.array([12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37])
print(x[::-1])

print("===================Ex 2=========================")
# Input arrays
arr1 = np.array([0, 10, 20, 40, 60])
arr2 = np.array([10, 30, 40])

result = np.isin(arr1, arr2)

print(result, end=" ")
print()

print("===================Ex 3=========================")
arr1 = np.array([1, 6, 4, 8, 9, -4, -2, 11])
vt_max = np.argmax(arr1)
vt_min = np.argmin(arr1)
max = np.max(arr1)
min = np.min(arr1)

print("Max = ",max," at ", vt_max)
print("Min = ",min," at ", vt_min)
print()

print("===================Ex 4=========================")
