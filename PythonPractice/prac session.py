arr = []
for i in range(5):
    num = int(input("enter the numbers"))
    arr.append(num)

arr.sort()
second_smallest = arr[1]
third_largest = arr[-3]

add = second_smallest + third_largest
print(add)

