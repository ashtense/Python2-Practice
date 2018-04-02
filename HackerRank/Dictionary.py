
dictionary_size = int(raw_input().strip())

name_directory = {}

for i in range(0, dictionary_size):
    arr_incoming = raw_input("").split(' ')
    name_directory[arr_incoming[0]] = int(arr_incoming[1])


while True:
    querry = raw_input("")
    if querry == "":
        break
    if name_directory.has_key(querry):
        print "%s=%r" % (querry, name_directory[querry])
    else:
        print "Not found"
