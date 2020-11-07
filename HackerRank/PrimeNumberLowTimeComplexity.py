import math

def checkPrime(incommingInt):
    if(incommingInt <= 1):
        return "Not prime"

    rootInt = int(math.sqrt(incommingInt))
    for index in range(2, rootInt+1):
        if(incommingInt % index == 0):
            return "Not prime"
    
    return "Prime"


sampleSpace = int(input())
arrInputs = []
for index in range(sampleSpace):
    arrInputs.append(int(input()))

for index in range(len(arrInputs)):
    print(checkPrime(arrInputs[index]))