import sys

num = 456489789
print(bin(num).replace("0b",""))

arr = []
arr_temp = [1,0,1,0,1,2]
for index in range(6):
    print(index)
    arr.append(arr_temp)

print(arr)