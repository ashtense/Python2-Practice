import sys

if __name__ == '__main__':
    pythonStudents = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        tempArr = [name, score]
        pythonStudents.append(tempArr)

# pythonStudents = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
lowest = second = sys.maxsize

for index in range(len(pythonStudents)):
    if pythonStudents[index][1]<lowest:
        second = lowest
        lowest = pythonStudents[index][1]
    elif pythonStudents[index][1] < second and pythonStudents[index][1] != lowest:
        second = pythonStudents[index][1]

secondLowestList = [x[0] for x in pythonStudents if x[1]==second]
secondLowestList.sort()
print ('\n'.join(secondLowestList))