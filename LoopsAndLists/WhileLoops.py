def populate_array(numbers, counter):
    while counter < 6:
        numbers.append(counter)
        counter = counter + 1


i = 0
numbers = []

populate_array(numbers, i)

print "After the loop value is %d" % i

for num in numbers:
    print "Running a loop on array %d" % num

print "Lets print the loop %r" % numbers
