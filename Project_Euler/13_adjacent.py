from sys import argv, exit
from check_integer import check_input_integer

"""
This reads a file and finds the largest product that can be had by multiplying
13 adjancent numbers.  The program needs the final line in the text to be blank.
"""

script, filename = argv

txt = open(filename)

reading = 1 #keeps track of if the file has concluded
array_of_digits = []
#converts our file to an array of digits
while(reading == 1):
    sequence = txt.readline()
    if sequence == '':
        reading = 0
    else:
        line = check_input_integer(sequence)
        for i in range(sequence.__len__()-1):
            array_of_digits.append(line % (10**(sequence.__len__()-1-i)) // 10**(sequence.__len__()-2-i))

biggest = 0
biggest_array = [0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(array_of_digits.__len__()-12):
    product = 1
    for j in range(13):
        product = product * array_of_digits[i+j]
    if biggest < product:
        biggest = product
        for k in range(13):
            biggest_array[k] = array_of_digits[i+k]

print(f"{biggest} is the product of {biggest_array}")
