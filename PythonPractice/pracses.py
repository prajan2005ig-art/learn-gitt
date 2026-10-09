def duplicate(arr):
    for num in arr:
        if arr.count(num) > 1:
            return num

arr = [0,1,2,3,4,5,6,7,8,9,6]
print(duplicate(arr))


