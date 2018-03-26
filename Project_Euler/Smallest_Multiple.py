from check_integer import check_input_integer

"""This program takes as input an integer less than 100.  It then proceeds to
calculate the smallest number which is divisible by every integer less than or
equal to the input integer."""

print("I shall find the smallest number which is divisible by every integer less than or equal to what positive integer?")
number = input("> ")

upper_bound = check_input_integer(number)

if upper_bound > 100:
    print("Input is too large.")

array_of_primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
powers = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#I find the largest powers of 2,3,5,7 that are less than upper_bound
for i in range(4):
    j = 0
    while array_of_primes[i]**(j+1) <= upper_bound:
        j +=1
    powers[i] = j
#the remaining primes can only have power at most 1
for i in range(4,25):
    if array_of_primes[i] <= upper_bound:
        powers[i] = 1

print(powers)
product = 1
for k in range(25):
    product = product*array_of_primes[k]**powers[k]
print(product)
