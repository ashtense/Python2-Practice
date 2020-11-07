def sort(arrayToSort):
    length = len(arrayToSort)
    swapCounter = 0
    for i in range(0, length):
        for j in range(0, length - 1):
            if arrayToSort[j] > arrayToSort[j+1]:
                tempNumber = arrayToSort[j]
                arrayToSort[j] = arrayToSort[j+1]
                arrayToSort[j+1] = tempNumber
                swapCounter += 1
    return swapCounter

arr = [2,1,3]
print("Array is sorted in %d swaps."%sort(arr))
print("First Element: %d" % arr[0])
print("Last Element: %d" % arr[len(arr)-1])