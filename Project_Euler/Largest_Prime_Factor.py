from sys import exit
import math
from check_integer import check_input_integer

"""
Finds the largest prime factor of an input integer.
"""

#a recursive function that takes two integers, composite and starter
#composite is the number who's largest prime factor we wish to know
#the program will run the first time with starter =2.
#we will check if composite is prime.  This can be accomplished
#by checking if any numbers divide composite which are smaller than
#the squareroot of composite.  If not then composite is prime and we are done
#if so, then we have found composite's smallest prime factor.  We may divide
#composite by this factor and run through the program again.  We do this
#until composite is prime (and thus we have our final answer)
def largest_prime_factor(composite, starter):
    #eliminates an abusrd case
     if composite == 1:
         print("This is not divisible by any prime.")
         exit(0)
    #once we have divided by i, we know that no smaller primes divide composite
    #by construction of the algorithm.  Thus we may tell the future iteration
    #of the recurrsion to ignore these numbers.
     i=starter
     upper_bound = math.floor(math.sqrt(composite))
     while i <= upper_bound:
         if composite % i == 0:
             new_composite = composite // i
             return largest_prime_factor(new_composite, i)
         else:
            i += 1
     #if we get here, the number was prime
     return composite

print("Please give me a positive integer.  I will find its largest prime factor.")
number = input("> ")

composite = check_input_integer(number)
print(largest_prime_factor(composite, 2))
