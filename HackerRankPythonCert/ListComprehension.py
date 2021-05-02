x = 2
y = 2
z = 2
n = 2

arrGrid = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z + 1):
            tempArr = [i,j,k]
            arrGrid.append(tempArr)
            

# print(arrGrid)
# secondLowestList = [x[0] for x in pythonStudents if x[1]==second]
newGrid = [x for x in arrGrid if x[0] + x[1] + x[2] != n]
# newGrid = [val for sublist in arrGrid]
print(newGrid)