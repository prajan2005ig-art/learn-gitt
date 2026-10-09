def firstnonrepeating(string):
    for char in string:
        if string.count(char) == 1:
            return char
    return  None

string = input("Enter a string: ")
print(firstnonrepeating(string))


