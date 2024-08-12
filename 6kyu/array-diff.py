def array_diff(a, b):
    return [i for i in [str(i) if i in b else i for i in a] if type(i) != str]

if __name__ == "__main__":
    print(array_diff([1,2,2], [2]))