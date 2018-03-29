def odd_even_index_function(dictionary_element):
    for element in dictionary_element.items():
        lst_even = []
        lst_odd = []
        for index in range(0, len(element[1])):
            if(index == 0):
                lst_even.append(element[1][index])
            elif(index % 2 == 0):
                lst_even.append(element[1][index])
            else:
                lst_odd.append(element[1][index])
        print ''.join(lst_even), ''.join(lst_odd)


number_of_cases = int(raw_input(""))

stuff = {}

for i in range(0, number_of_cases):
    my_string = raw_input("")
    stuff[i] = list(my_string)

odd_even_index_function(stuff)
