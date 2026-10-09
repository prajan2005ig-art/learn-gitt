stack = []

stack.append(1)
stack.append(2)
stack.append(3)
print(stack)

stack.pop()
print(stack)
stack.reverse()
print(stack)
stack.reverse()
print(stack)
stack.append(4)
stack.append(5)
print(stack[-1])
stack.append(6)
stack.append(7)
print(stack)
if stack == []:
    print("Stack contains element")
else:
    print("Stack is empty")
stack.remove(4)
print(stack)