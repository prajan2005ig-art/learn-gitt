def lcs(arr):
    s = set(arr)
    longest = 0

    for num  in s:
        if num - 1 not in s:
            count = 1

        while num + count in s:
            count += 1

        result = max(count, longest)
        return result

arr = [1,2,4,5,6,3,9,23,45]
print(lcs(arr))


