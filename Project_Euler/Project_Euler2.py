from check_integer import check_input_integer

"""
Summing the even valued Fibonocci numbers that are smaller than 4 million
"""

print("I shall find the sum of all even Fibonocci numbers below what positive integer?")
number = input("> ")

upper_bound = check_input_integer(number)

#initial Fibonocci
sum = 0 # start with 2 so we can work more comfortably always ahving two odds behind
first_odd_value = 1
second_odd_value = 1
even_value = 2

#actually computes the sum
while even_value < upper_bound:
    sum += even_value
    first_odd_value = second_odd_value+even_value
    second_odd_value = even_value+first_odd_value
    even_value = first_odd_value+second_odd_value

print(sum)
