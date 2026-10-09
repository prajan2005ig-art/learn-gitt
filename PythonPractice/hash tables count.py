arr = [1,2,2,2,3,2,3,3,3,4,4,6,5,4]

count = {}

for num in arr:
    if num in count:
        count[num] += 1

    else:
        count[num] = 1

print(count)