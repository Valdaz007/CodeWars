## Description
# Examples below show you how to write function accum:
# 
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"

def accum(st):
    ## Normal For Loop
    # temp = []
    # for i,j in enumerate(st,1):
    #     temp.append((j*i).capitalize())
    # return '-'.join(temp)

    
    # List Comprehension
    return '-'.join((j*i).capitalize() for i,j in enumerate(st, 1))

print(accum('RqaEzty'))