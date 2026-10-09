number = [2,4,5,6,7,8,9,4,5,90,6]
n = len(number)

for i in range(n):
    min_index = i
    for j in range(i+1,n):
        if number[j] < number[min_index]:
            min_index = j

    number[i], number[min_index] = number[min_index], number[i]

print(number)

