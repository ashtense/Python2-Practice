class AdvancedArithmetic(object):
    def divisorSum(self, n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        divisorSum = 0
        for index in range(1, n+1):
            if n % index == 0:
               divisorSum = divisorSum + index
        return divisorSum

obj = Calculator()
print(obj.divisorSum(6))