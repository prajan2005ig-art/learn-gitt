def freq(s):
    words = s.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word,0)+1
    return freq

s = input("enter string")
print(freq(s))