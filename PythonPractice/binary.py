number = [1,2,3,4,5,5,6]
target = 3

low = 0
high = len(number) - 1
found = False

while low <= high:
    mid =(low + high) // 2
    if number[mid] == target:
        print("found")
        found = True
        break

    elif number[mid] > target:
        high = mid - 1

    else:
        low = mid + 1

if found == False:
    print("not found")
