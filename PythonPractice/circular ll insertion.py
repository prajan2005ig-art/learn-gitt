from operator import truediv


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
data5.next = data6
data6.next = head

current = head

data0 = node(0)

while current.next != head:#insertion at first
    current = current.next

data0.next = head
current.next = data0
head = data0

current = head

data7 = node(7)
while current.next != head:#insertion at last
    current = current.next

current.next = data7
data7.next = head

current = head

data30 = node(30)
for i in range(4):#insertion at given position
    current = current.next

data30.next = current.next
current.next = data30

current = head

data8 = node(8)
while current.data != 6:#insertion after a current data
    current = current.next
data8.next = current.next
current.next = data8

current = head


while True:#traversal
    print(current.data)
    current = current.next

    if current == head:
        break