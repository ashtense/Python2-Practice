# O(n) time complexity, n being the limit of integers
# O(n) space complexity, n being the limit of integers
class FizzBuzz(object):
    resultString = ""
    def __init__(self, number):
        if number % 3 == 0 and number % 5 == 0:
            self.resultString = (" %s FizzBuzz" % number)
        elif number % 3 == 0:
            self.resultString = (" %s Fizz" % number)
        elif number % 5 == 0:
            self.resultString = (" %s Buzz" % number)
        else:
            self.resultString = (" %s" % number)


limit = 15
for number in range(1,limit+1):
    firstObject = FizzBuzz(number)
    print(firstObject.resultString)