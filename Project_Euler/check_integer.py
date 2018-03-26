from sys import exit

"""
Checks that input is a positive integer.  This will be useful throughout these
Project Euler problems.
"""

def convert_integer(s):
  try:
      return int(s)
  except ValueError:
      return None

#checks for proper input
def check_input_integer(number):
    pos_int = convert_integer(number)
    if pos_int == None:
        print("You need to give me an integer.")
        exit(0)
    elif pos_int < 1:
        print("You need to give me a positive integer.")
        exit(0)
    else:
        return pos_int
