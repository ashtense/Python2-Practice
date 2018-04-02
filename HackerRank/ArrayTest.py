def reverse_array(original_array):
    lst_reversed = []
    for element in reversed(original_array):
        lst_reversed.append(str(element))
    print ' '.join(lst_reversed)


n = nt(raw_input().strip())
lst_integer = map(int, raw_input().strip().split(' '))

reverse_array(lst_integer)
