import sys

arr = []
for arr_i in xrange(6):
    arr_temp = map(int, raw_input().strip().split(' '))
    arr.append(arr_temp)

max_sum = 0
for row_num in range(0, 4):
    for col_num in range(0, 4):
        hour_glass_sum = 0
        hour_glass_sum = arr[row_num][col_num] + arr[row_num][col_num + 1] + \
            arr[row_num][col_num + 2] + arr[row_num + 1][col_num + 2] + \
            arr[row_num + 2][col_num] + arr[row_num + 2][col_num + 1] + \
            arr[row_num + 2][col_num + 2]
        if hour_glass_sum > max_sum:
            max_sum = hour_glass_sum

print max_sum
