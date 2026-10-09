def parantheses(s):
    stack = []
    pairs ={']':'[','}':'{',')':'('}
    for char in s:
        if char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
        else:
            stack.append(char)

    return len(stack) == 0

s = '[{()}]'
print(parantheses(s))