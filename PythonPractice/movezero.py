def movezero(arr):
    result = []
    for num in arr:
        if num != 0:
            result.append(num)
    for num in arr:
        if num == 0:
            result.append(num)
    return result

arr = list(map(int,input("Enter a list: ").split()))
print(movezero(arr))