'''
Created on Oct 5, 2017

@author: solanka
'''

x = "There are %d types of people in my company" % 4
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s know %s are" % (binary, do_not, binary);
print x
print y

# sometimes qualifiers convert values on some basis. Boolean if provided on integer qualifier i.e. %d will convert it into 1 or 0
z = "This is boolean check %r"
hilarious = False
print z % hilarious

# this is great. I can combine stuff from different strings along with their qualifiers spot on.
print z % hilarious + "." + x

print "Hello %s" % "Ashwani"
print "Hello " * 3

print "A quick brown fox jumps \nover the lazy dog."
print """Road to salvation begins \a tonight!!!
Right now.
"""