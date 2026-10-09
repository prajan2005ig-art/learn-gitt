def duplicate(arr):
    seen = set()
    for char in arr:
        if char in seen:
            return char
        seen.add(char)
    return None

arr = [0,1,2,3,4,5,6,7,8,9,6,]
print(duplicate(arr))