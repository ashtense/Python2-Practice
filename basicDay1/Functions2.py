def add(a, b):
    print "adding %d & %d" % (a, b)
    return a + b


def subtract(a, b):
    print "subtracting %d from %d" % (b, a)
    return a - b


def multiply(a, b):
    print "multiplying %d into %d" % (a, b)
    return a * b


def division(a, b):
    print "Dividing %d by %d" % (a, b)
    return a / b


print "lets do something with these functions"

age = add(20, 6)
height = subtract(8, 2)
weight = multiply(90, 2)
iq = division(100, 2)

print "age: %d , height: %d, weight: %d and iq: %d" % (age, height, weight, iq)

varWhitaker = add(age, subtract(height, multiply(weight, division(iq, 2))))

print "it becomes %d" % varWhitaker
