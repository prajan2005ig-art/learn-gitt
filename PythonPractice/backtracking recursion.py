def generate(s,path):
    if len(path) == len(s):
        print(path)
        return

    for char in s:
        if char not in path:
            generate(s,path+char)

print(generate("ab",""))


