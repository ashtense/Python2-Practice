animals = ['bear', 'dog', 'elephant', 'whales', 'dinosaurs']
print "First animal is %s" % animals[0]

print "4th animal is %s" % animals[3]

# here we print subset of a list. It excludes item at \
# the second position given. weird
print (animals[1:3])

to_do = ['run', 'cleanup']
# lists inside a list is also permitted. neat
final_list = [to_do, animals]
print (final_list[1][2])
final_list.append('Geronimo')
print (final_list)
to_do.insert(1, 'wakeup')
print (to_do)
print ("Max method on list", max(to_do))
print ("Min method on list", min(to_do))
to_do.remove('wakeup')
print (to_do)
to_do.reverse()
print (to_do)
# This is how we remove elements based on index
del to_do[1]
print (to_do)
# to find the length of a list
print (len(final_list))
