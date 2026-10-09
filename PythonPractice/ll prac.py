class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# Create nodes
head = Node(10)

node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# Connect nodes
head.next = node2
node2.prev = head

node2.next = node3
node3.prev = node2

node3.next = node4
node4.prev = node3


# Reverse the doubly linked list
current = head

while current:
    current.next, current.prev = current.prev, current.next

    if current.prev is None:
        head = current

    current = current.prev


# Print reversed list
current = head

while current:
    print(current.data, end=" ")
    current = current.next