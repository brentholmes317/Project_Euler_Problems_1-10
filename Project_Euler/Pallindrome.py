"""This program will  find the largest pallindromic product of two three digit
numbers"""

#this program checks whether a 5-6 digit number is a pallindrome
def is_pallindrome(number):
    #first we find if it is a 5 or 6 digit number
    if number // 100000 == 0:
        d5 = number // 10000
        d4 = (number % 10000) // 1000
        d2 = (number % 100) // 10
        d1 = number % 10
        if d5 == d1 and d4 == d2:
            return True
        else:
            return False
    else:
        d6 = number // 100000
        d5 = (number % 100000) // 10000
        d4 = (number % 10000) // 1000
        d3 = (number % 1000) // 100
        d2 = (number % 100) // 10
        d1 = number % 10
        if d6 == d1 and d5 == d2 and d4 == d3:
            return True
        else:
            return False

i = 999
j = 999
cap = 0
tentative_answer = [0,0,0]

while i > cap:
  while j > cap:
    if is_pallindrome(i*j) == True:
      if i*j > tentative_answer[0]:
        tentative_answer = [i*j,i,j]
      cap = j
    j -= 1
  i -= 1
  j = i

if tentative_answer[0] == 0:
    print("No such pallindrome")
else:
    print(f"The largest pallindrome is {tentative_answer[0]} which is the product of {tentative_answer[1]} and {tentative_answer[2]}")
