# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

# Examples:

# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false

def long_solution(text, ending):
  if ending in text[-len(ending):]:     # using the 'len()' we can get the number of characters in the ending variable
    return True                         # and using text[-len(ending):] - we compare with the last character numbers that correspond to number of characters in ending
  else:
    return False

def solution(text, ending):
  return True if ending in text[-len(ending):] else False
