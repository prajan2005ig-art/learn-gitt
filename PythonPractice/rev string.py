def reverese(string):
    rev = ""
    for char in string:
        rev = char + rev
    return rev

string = input("enter string")
print(reverese(string))


