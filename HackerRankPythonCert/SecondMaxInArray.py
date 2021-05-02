import sys

arr = [2,3,6,6,5]
first = second = -sys.maxsize
for score in arr:
    if score > first:
        second = first
        first = score
    elif score > second and score != first:
        second = score

print(second)