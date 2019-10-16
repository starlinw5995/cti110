# This program displays a hollow stair-step pattern.
# 10/13/2019
# CTI-110 P4HW3 - Nested Loops
# William Starling
#
# This program displays a hollow stair-step pattern.

# The number of rows is named base_size.
base_size = 6

# Print a # for the number of rows in the range.
for row in range(base_size):
    print('#',end='')

# Print a space for the number of rows in a range.
    for column in range(row):
        print(' ',end='')

# Print a # a the end of the last space in a row.
    print('#')
