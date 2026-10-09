class node:
    def __init__(self,data):
        self.data = data
        self.next = None

data1 = node(1)
data2 = node(2)
data3 = node(3)
data4 = node(4)
data5 = node(5)
data6 = node(6)

head = data1

data1.next = data2
data2.next = data3
data3.next = data4
data4.next = data5
data5.next = head

current = head
previous = None
first = head

while True:
    new_node = current.next
    current.next = previous
    previous = current
    current = new_node

    if current == head:
        break

first.next = previous
head = previous

current = head

while True:
    print(current.data)
    current = current.next

    if current == head:
        break