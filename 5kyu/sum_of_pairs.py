# Sum of Pairs
# Given a list of integers and a single sum value, return the first two values (parse from the left please) in order of appearance that add up to form the sum.

# If there are two or more pairs with the required sum, the pair whose second element has the smallest index is the solution.

# Negative numbers and duplicate numbers can and will appear.

# NOTE: There will also be lists tested of lengths upwards of 10,000,000 elements. Be sure your code doesn't time out.

def sum_pairs(ints, s):
    myList = {j:[ints[i],ints[j]] for i in range(len(ints[:-1])) for j in range(i+1,len(ints)) if ints[i]+ints[j]==s}
    if len(myList): return myList[sorted(myList)[0]]
    return None
