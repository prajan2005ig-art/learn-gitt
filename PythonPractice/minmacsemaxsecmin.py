def minmax(arr):
    if len(arr) < 4:
        return "the array should at least contains 4 values"
    minval = float("inf")
    maxval = float("-inf")
    secmax = float("-inf")
    secmin = float("inf")
    for num in arr:
        if num > maxval:
            secmax = maxval
            maxval = num

        elif num > secmax and num != maxval:
            secmax = num

        if num < minval:
            secmin = minval
            minval = num

        elif num < secmin and num != minval:
            secmin = num

    return minval, maxval, secmin, secmax

arr = [10, 20, 30,70]
print(minmax(arr))

