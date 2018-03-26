from sys import exit
import math
from check_integer import check_input_integer

"""Takes an integer as input, k, as input and finds the sum of all primes below k."""

def is_prime(number):
    #if no number smaller than or equal to the squareroot divides a number it is prime
    upper_bound = math.floor(math.sqrt(number))
    for i in range(2, upper_bound+1):
        if number % i == 0:
            return False
    #if we get here, the number was prime
    return True

print("""I shall sum primes below what number?""")
number = input("> ")

k = check_input_integer(number)

#we wish to only check odd numbers for primes so we do 2 separately
if k == 1 or k==2:
    print(0)
    exit(0)
elif k == 3:
    print(2)
    exit(0)

potential_prime = 1
sum = 2

while potential_prime < k-2:
    potential_prime += 2
    if is_prime(potential_prime):
        sum += potential_prime

print(sum)
