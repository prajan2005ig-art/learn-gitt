def secondlargest(arr):
    if len(arr) < 2:
        return None

    largest = float('-inf' )
    second_largest = float('-inf')

    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest

arr = [1,2,3,4,5,6,7,8,9]
print(secondlargest(arr))






