# Kata Title: String Incrementer
# Your job is to write a function which increments a string, to create a new string.

# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.
# Examples:

# foo -> foo1

# foobar23 -> foobar24

# foo0042 -> foo0043

# foo9 -> foo10

# foo099 -> foo100

# Attention: If the number has leading zeros the amount of digits should be considered.

def increment_string(strng):
    print(strng)
    count = numCount(strng)
    if count == 0:
        return f"{strng}1"
    strInc = zero(strng[-count:])
    return f"{strng[:-count]}{strInc}"

def zero(temp):
    if temp[0] == "0" and len(temp) == 1:
        return "1"
    elif temp[0] == "0":
        strnum = zero(temp[1:])
        return f"0{strnum}" if len(strnum) < len(temp) else strnum
    else:
        return f"{int(temp)+1}"

def numCount(strline):
    numcount = 0
    for i in strline:
        if i in "1234567890": numcount += 1
        else: numcount = 0
    return numcount
