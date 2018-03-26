from check_integer import check_input_integer

"""This program takes as input an integer less than 1000, k.  It then
proceeds to calculate the difference between the sum of the squares of the
first k natural numbers and the square of the sum."""

print("""I shall find the the difference between the sum of the squares of the
first k natural numbers and the square of the sum.  What k should I use?""")
number = input("> ")

k = check_input_integer(number)

if k > 1000:
    print("Input is too large.")

sum_of_squares = 0
for i in range(k):
    sum_of_squares += (i+1)**2

answer = ((k*(k+1))/2)**2 - sum_of_squares
print(answer)
