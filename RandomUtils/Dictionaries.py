def print_values(stuff_dictionary):
    i = 1
    for value in stuff_dictionary.values():
        print "Value %d: %r" % (i, value)
        i = i + 1


def print_keys(stuff_dictionary):
    i = 1
    for key in stuff_dictionary.keys():
        print "Key %d: %r" % (i, key)
        i = i + 1


stuff = {'first_name': "Ashwani", 'last_name': 'Solanki', 'age': 26}

print stuff['first_name']
print stuff['last_name']
print "His age is %d" % stuff['age']

stuff[1] = "Wow"

print_keys(stuff)
print_values(stuff)
