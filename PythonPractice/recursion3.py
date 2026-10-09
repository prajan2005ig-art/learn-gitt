def sumn(n):
    if n == 0:
        return 0

    return n + sumn(n-1)
print(sumn(5))