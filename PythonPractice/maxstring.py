def strmax(string):
    maxcount = 0
    maxchar = ""
    for char in string:
        count = string.count(char)

        if count > maxcount:
            maxcount = count
            maxchar = char
    return maxchar

string = "aaaacccccccccabde"
print(strmax(string))



