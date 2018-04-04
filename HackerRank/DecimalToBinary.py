n = 439
lst_binary = []

while True:
    lst_binary.append(n % 2)
    if n != 0:
        n = n / 2
    else:
        break

consecutive_counter = 1
highest_counter = 0

for bit_position in range(0, len(lst_binary)):
    if lst_binary[bit_position] is 1 and bit_position < (len(lst_binary) - 1):
        if lst_binary[bit_position] == lst_binary[bit_position + 1]:
            consecutive_counter += 1
    elif lst_binary[bit_position] == 0:
        consecutive_counter = 1
    if consecutive_counter > highest_counter:
        highest_counter = consecutive_counter

print highest_counter
