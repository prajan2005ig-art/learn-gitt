def rev_string(string):
    if string == "":
        return ""

    return rev_string(string[1::]) + string[0]
print(rev_string("hello"))

