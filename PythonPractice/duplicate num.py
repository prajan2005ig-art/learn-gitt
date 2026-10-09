def duplicate(arr):
    seen = set()
    duplicate = []
    for num in arr:
        if num not in seen:
            seen.add(num)
        else:
            duplicate.append(num)
    return duplicate

arr = [0,0,1,2,5,3,4,5,6,7,8,9]
print(duplicate(arr))