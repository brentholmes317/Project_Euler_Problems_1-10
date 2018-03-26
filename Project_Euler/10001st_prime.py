from sys import exit
import math
from check_integer import check_input_integer

"""Takes an integer k as input and finds the kth prime."""

def is_prime(number):
    #if no number smaller than or equal to the squareroot divides a number it is prime
    upper_bound = math.floor(math.sqrt(number))
    for i in range(2, upper_bound+1):
        if number % i == 0:
            return False
    #if we get here, the number was prime
    return True

print("""Which prime shall I find?""")
number = input("> ")

k = check_input_integer(number)
#we wish to only check odd numbers for primes so we do 2 separately
if k == 1:
    print(2)
    exit(0)

counter = 2
prime = 3

while counter < k:
    prime += 2
    if is_prime(prime):
        counter += 1



print(prime)
