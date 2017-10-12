'''
Created on Oct 10, 2017

@author: solanka
'''
from os.path import exists

print "We will copy files from one another. Hit Enter!!"
raw_input("")
in_file = open('ABC.txt')
in_files_data = in_file.read()

to_file = 'DEF.txt'

print "Input from file1 is %d" % len(in_files_data)

print "Does the output file exits. %s" % exists(to_file)

out_file = open(to_file, 'w+')
out_file.write(in_files_data)

print "Does the output file exits. %s" % exists(to_file)

in_file.close()
out_file.close()