from functools import total_ordering


def findmissing(arr):
    n = len(arr) + 1

    total = n * (n + 1) // 2
    for num in arr:
        total -= num
    return total

arr = [1,2,3,5,6,7]
print(findmissing(arr))