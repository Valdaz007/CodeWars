def increment_string(strng):
    strli = "".join([i for i in strng if i not in "1234567890"])
    intli = [i for i in strng if i in "1234567890"]
    print(intli, strli)

    if len(intli) == 0: intli = "1"
    else: intli = int("".join(intli))+1
    return '{:0=3d}'.format(intli)

print(increment_string("foo010"))