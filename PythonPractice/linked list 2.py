class nodes:
    def __init__(self,data):
        self.data = data
        self.next = None

node1 = nodes(2)
node2 = nodes(3)
node3 = nodes(4)

head = node1

node1.next = node2
node2.next = node3

new_node = nodes(5)#inserting node at first
new_node.next = head
head = new_node

current = head

newnode = nodes(34)

while current.next:# to insert at last
    current = current.next
current.next = newnode

current = head#to reset current at head position

newnode2 = nodes(25)
while current.data != 4:#insert after 4
    current = current.next

newnode2.next = current.next
current.next = newnode2

current = head#reset

position = 3#defing position
newnode3 = nodes(234)

for i in range(position - 2):#new position insertion
    current = current.next

newnode3.next = current.next
current.next = newnode3

current = head

while current:
    print(current.data)
    current = current.next
