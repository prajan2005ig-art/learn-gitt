arr =[1,2,3,3,3,4,4,5,6,7,8,9,1,12,13]

count = {}

for num in arr:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

for num in arr:
    if count[num] == 1:
        print(num)
        break

