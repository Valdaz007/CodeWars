# Vowel Count
# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.

def get_Count(sentence: str) -> int:
  return len([i for i in sentence if i in "aeiuo"])

if __name__ == "__main__":
  get_Count('hello')
  
  
  
# Expected Output: 2
