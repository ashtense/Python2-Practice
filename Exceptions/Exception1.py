def conver_number(incomming_number):
    try:
        return int(incomming_number) * 2
    except ValueError:
        return 6


print conver_number("Geronimo")
print conver_number(5)
