ten_things = "Apples oranges crows telephone light sugar"

print "Wait there's not 10 things in that list. lets fix that!!"

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Evening", "Geronimo", "THC", "Uncle Joey"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding %s" % next_one
    stuff.append(next_one)
    print "there are %d items now" % len(stuff)

print "There we go: ", stuff

print "Lets do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
# join the elements in array called stuff
print ' '.join(stuff)
# join the elements on 3rd and 5th position via #
print '--'.join(stuff[3:5])

# this way of fetching elements from array works only on 2 elements.
# below way of trying 3 elements doesn't work.

print stuff[3:5:1]
