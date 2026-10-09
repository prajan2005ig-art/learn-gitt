def max3(arr):
    max = float("-inf")
    smax = float("-inf")
    tmax = float("-inf")
    for num in arr:
        if num > max:
            tmax = smax
            smax = max
            max = num

        elif num > smax and num != max:
            tmax = smax
            smax = num


        elif num > tmax and num != smax:
            tmax = num


    return tmax

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(max3(arr))
