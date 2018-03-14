
the_count = [1, 2, 3, 4, 5]
fruits = ['bananas', 'apples', 'guava']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']


for loopVariable in the_count:
    print "This is the count %d" % loopVariable

for fruit in fruits:
    print "I like this fruit %s" % fruit

for changeLoop in change:
    print "I got %r" % changeLoop

# We can also initialize the list and fill in values later on.
elements = []

# range function, returns a list based on start_stop
# parameters you've provided.

for i in range(0, 6):
    elements.append(i)

for i in elements:
    print "Here is %d" % i

print "This is a list %r " % range(1, 3)
