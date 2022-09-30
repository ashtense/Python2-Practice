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

arr = [20,35,-15,7,55,1,-22]
sort(arr)
print(arr)