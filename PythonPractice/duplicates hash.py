arr = [1,2,2,3,4,5,5,5,6,5,5,7,]

seen = set()

for num in arr:
    if num in seen:
        print("duplicate",num)

    else:
        seen.add(num)
print(seen)
