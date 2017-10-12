'''
Created on Oct 9, 2017

@author: solanka
'''
filename = raw_input("Please enter file Name")

txt = open(filename, 'r+')

print "Here is your fileName %s \n Now we will erase this file. Press enter if you want to do." % filename

raw_input("?")

txt.truncate()

print "Now we write new stuff in the file."
inputContent = raw_input()
txt.write(inputContent)

readStuff = txt.read()

print "This is what you wrote in the file. \n %s" % readStuff

txt.close()
