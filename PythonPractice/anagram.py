def anagram(string1,string2):
    if len(string1) != len(string2):
        return False
    else:
        count1 = {}
        count2 = {}
        for char1 in string1:
            count1[char1] = count1.get(char1,0)+1
        for char2 in string2:
            count2[char2] = count2.get(char2,0)+1

        if count1 == count2:
            print("anagaram")
        else:
            print("not anagram")

string1 = input("enter string")
string2 = input("enter string")
anagram(string1,string2)



