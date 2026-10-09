number = [1,2,3,4,5,6]
target = 3
found = False

for i in range(len(number)):
    if number[i] == target:
        print("found at index : ",i)
        found = True
        break
if found == False:
    print("not found")