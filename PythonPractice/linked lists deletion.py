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
data7 = node(7)
data8 = node(8)
data9 = node(9)
data10 = node(10)

head = data1

data1.next = data2
data2.next = data3
data3.next = data4
data4.next = data5
data5.next = data6
data6.next = data7
data7.next = data8
data8.next = data9
data9.next = data10

current = head

head = head.next#to delete the first node

current = head

while current.next.next is not None:#to delete the last node
    current = current.next

current.next = None
current = head

#to remove from specific location

position = 3

for i in range(position - 2):
    current = current.next

current.next = current.next.next

current = head

while current:
    print(current.data)
    current = current.next


