class node:
    def __init__(self,data):
        self.data = data
        self.next = None

node1 = node(2)
node2 = node(3)
node3 = node(4)
node4 = node(5)
node5 = node(6)
node6 = node(7)

head = node1

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

current = head

new_node = node

while current:
    print(current.data, end="->")
    current = current.next
print("null")

print(current)


