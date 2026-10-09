def duplicate(arr):
    duplicate = []
    for num in arr:
        if arr.count(num) > 1 and num not in duplicate:
            duplicate.append(num)
    return duplicate



arr = [0,1,2,3,4,5,6,7,8,9,9,9,2,4,5,6]
print(duplicate(arr))