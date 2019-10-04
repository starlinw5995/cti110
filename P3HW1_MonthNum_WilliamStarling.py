#CTI - 110
#P3HW1 - Month number
#William Starling
#10-03-2019
#
# Input month number (1-12).
month = int(input('Enter the month number: '))

# Tell the name of the month by the number.
if month == 1:
    print('January')
if month == 2:
    print('February')
if month == 3:
    print('March')
if month == 4:
    print('April')
if month == 5:
    print('May')
if month == 6:
    print('June')
if month == 7:
    print('July')
if month == 8:
    print('August')
if month == 9:
    print('September')
if month == 10:
    print('October')
if month == 11:
    print('November')
if month == 12:
    print('December')
if month > 12:
    print('Error Message')
if month < 1:
    print('Error Message')
