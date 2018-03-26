from check_integer import check_input_integer

"""
Find the sum of all the multiples of 3 or 5 below 1000.
We shall generalize to give the answer for a user input.
"""

print("I shall find the sum of all multiples of 3 or 5 below what positive integer?")
number = input("> ")

upper_bound = check_input_integer(number)

#finds how many items we need to sum
upper_bound_five = (upper_bound-1) // 5  #if the input is 1000, we want to avoid adding 1000
upper_bound_three = (upper_bound-1) // 3
upper_bound_fifteen = (upper_bound-1) //15

sum = 0
for i in range(upper_bound_five):
    sum += (i+1)*5 #+1 makes it goe from 1 to upper_bound_five
for j in range(upper_bound_three):
    sum += (j+1)*3
#this gets rid of what we have double counted
for k in range(upper_bound_fifteen):
    sum -= (k+1)*15
print(sum)
