n = int(input("enter the number"))
count = 0
for i in range (1,n+1):
    if n % i == 0:
        count += 1

if count == 2:
    print("it is prime")
elif count == 1:
    print("it is composite")
else :
    print("it is not prime")
