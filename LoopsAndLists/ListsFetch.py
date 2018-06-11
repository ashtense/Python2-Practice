animals = ['bear', 'dog', 'elephant', 'whales', 'dinosaurs']
print "First animal is %s" % animals[0]

print "4th animal is %s" % animals[3]

# here we print subset of a list. It excludes item at \
# the second position given. weird
print animals[1:3]

to_do = ['run', 'cleanup']
# lists inside a list is also permitted. neat
final_list = [to_do, animals]

print final_list
