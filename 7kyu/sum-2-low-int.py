## Description
# Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. 
# No floats or non-positive integers will be passed.
# For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[0:2])

# Test
print(sum_two_smallest_numbers([8,2,9,1]))