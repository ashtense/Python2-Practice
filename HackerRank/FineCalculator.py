from datetime import date

def calculateFine(actualDate, expectedDate):
    if actualDate <= expectedDate:
        return 0
    elif actualDate > expectedDate:
        if actualDate.year == expectedDate.year:
            if actualDate.month == expectedDate.month:
                deltaDays = (actualDate - expectedDate).days
                return  15 * deltaDays
            else:
                deltaMonths = actualDate.month - expectedDate.month
                return 500 * deltaMonths
        else:
            return 10000


# actualDate = date(year = 2020, month = 11, day = 22)
# expectedDate = date(year = 2020, month = 11, day = 22)
# print(calculateFine(actualDate, expectedDate))

actualDate = None
expectedDate = None
for index in range(1):
    if(actualDate is None):
        date_incomming = list(map(int, input().split()))
        day = date_incomming[0]
        month = date_incomming[1]
        year = date_incomming[2]
        actualDate = date(year = year, month = month, day = day)
    date_incomming = list(map(int, input().split()))
    day = date_incomming[0]
    month = date_incomming[1]
    year = date_incomming[2]
    expectedDate = date(year = year, month = month, day = day)

print(calculateFine(actualDate, expectedDate))
# print(actualDate)
# print(expectedDate)