def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[0:2])

print(sum_two_smallest_numbers([8,2,9,1]))