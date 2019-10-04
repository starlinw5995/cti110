# Calculate area of two rectangles and tell which one has greater area.
# 10-3-19
# CTI-110 P3T1 - Areas of Rectangles
# William Starling
#
# Length and width of rectangle 1.
length1 = int(input('Enter length of rectangle 1: '))
width1 = int(input('Enter width of rectangle 1: '))

# Length and width of rectangle 2.
length2 = int(input('Enter length of rectangle 2: '))
width2 = int(input('Enter width of rectangle 2: '))

# Calculate the area of the rectangles.
area1 = length1 * width1
area2 = length2 * width2

# Tell which has a greater area.
if area1> area2:
    print('Rectangle 1 has the greater area.')
elif area2 > area1:
    print('Rectangle 2 has the greater area.')
else:
    print('Both have the same area.')
    
