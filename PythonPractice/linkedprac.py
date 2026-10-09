class Node :
    def __init__(self,data):
        self.data = data
        self.next = None

node1 = Node(23)
node2 = Node(24)
node3 = Node(25)
node4 = Node(26)
node5 = Node(27)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

max_value = node1.data
current = node1.next

while current:
    if current.data > max_value:
        max_value = current.data
    current = current.next

print(max_value)