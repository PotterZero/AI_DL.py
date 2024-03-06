print("========== EX 1 ==========")
data1 = [-10, -21, -4, -45, -66, 93, 11, -4, -6, 12, 11, 4]
def SOAM():
    so_am = 0
    for i in data1:
        if i < 0:
            so_am += 1
            print("{}".format(i),end=" ")
    return so_am
def SoDuong():
    so_dương = 0
    for i in data1:
        if i >0:
            so_dương += 1
            print("{}".format(i), end=" ")
    return so_dương

print("\nSo am :",SOAM())
print()
print("\nSo duong : ", SoDuong())
print()


print("========== EX 2 ==========")
data2 = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
dem = 0
#x = int(input("Nhap so k = "))
x= 3
for i in data2:
    if i == x:
        dem +=1
print("So lan xuat hien là :",dem)
print()

print("========== EX 3 ==========")
data3 = [4, 5, 6, 7, 3, 9, 11, 2, 10]

for i in range(len(data3)-1):
    current = (data3[i], data3[i+1])
    max_value = max(current)
    print(f"MAX {current} is {max_value}")
print()


print("========== EX 4 ==========")
data4 = [1, 2, 3]

for i in data4:
    for j in data4:
        for k in data4:
            print(f"{i},{j},{k}")
print()

print("========== EX 5 ==========")
test_list1 = [[4, 3, 5], [1, 2, 3], [3, 7, 4]]
test_list2 = [[1], [9], [8]]

result_matrix = []

for i in range(len(test_list1)):
    result_row = test_list1[i] + test_list2[i]
    result_matrix.append(result_row)

print("Result Matrix:")
for row in result_matrix:
    print(row)
print()

print("========== EX 6 ==========")
for i in range(2001, 3200):
    if i % 5 !=0 and i % 7 == 0:
        print(f"So chi chia het cho 7 la {i}")
print()

print("========== EX 7 ==========")
def check_num(num):
    for digit in str(num):
        if int(digit) % 2 != 0:
            return False
    return True

KQ = [str(num) for num in range(1000,3001) if check_num(num)]

print(KQ)