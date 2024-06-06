## Description
# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. 
# Essentially, rearrange the digits to create the highest possible number.

def descending_order(num: int) -> int:
    return int("".join([i for i in sorted(str(num))[::-1]]))


#Test
print(descending_order(357832))