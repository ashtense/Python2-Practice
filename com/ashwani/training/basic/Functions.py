'''
Created on Oct 11, 2017

@author: solanka
'''
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %s, arg2: %s" % (arg1, arg2)
# Indentation is really important here. 4 spaces right from left should be the indentation on an instruction for it to be a part of function.
     
def print_two_java_way(arg1, arg2):
    print "arg1: %s, arg2: %s" % (arg1, arg2)
    
    
print_two("Ashwani", "Solanki")
print_two_java_way("Chaudhary", "Singh")
