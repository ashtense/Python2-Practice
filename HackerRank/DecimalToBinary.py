incomming_decimal = 13
remaining_dividend = 0
binary_place = []

while True:
    binary_place.append(incomming_decimal % 2)
    if incomming_decimal != 0:
        incomming_decimal = incomming_decimal / 2
    else:
        break
binary_place.reverse()
print binary_place

for bit_position in range(0, len(binary_place)):
    print binary_place[bit_position]
