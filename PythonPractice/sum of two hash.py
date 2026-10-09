arr = [1,2,3,4,3,67,8,9,6,5,4,3]

target = 10
seen = set()

for num in arr:
    need = target - num

    if need in seen:
        print(num,need)
        break
    seen.add(num)
