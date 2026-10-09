def chartype(string):
    upper = 0
    lower = 0
    digits = 0
    special = 0
    for char in string:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isdigit():
            digits += 1
        else:
            special += 1
    print(f"uppercase:{upper},lowercase:{lower},digits:{digits},special:{special}")

string = "helloSDF2345@#$"
chartype(string)