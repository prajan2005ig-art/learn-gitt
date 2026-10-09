number = [1,4,6,8,9,2,3,90,89,67]
n = len(number)

for i in range(n):
    for j in range (0,n-i-1 ):
        if number[j] > number[j + 1]:
            number[j], number[j + 1] = number[j + 1], number[j]
print(number)