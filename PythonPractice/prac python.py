def anagram(s1,s2):
    s1=s1.upper()
    s2=s2.upper()
    freq = {}
    if len(s1)!=len(s2):
        return False

    for char in s1:
        if char in freq:
            freq[char] +=1
        else:
            freq[char] = 1


    for char in s2:
        if char not in freq:
            return False

        freq[char] -= 1

        if freq[char] < 0:
            return False
    return True

s1 = input("enter string")
s2 = input("enter string")

print(anagram(s1,s2))
