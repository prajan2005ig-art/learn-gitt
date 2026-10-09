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

head = data1

data1.next = data2
data2.next = data3
data3.next = data4
data4.next = data5
data5.next = data6
data6.next = data7

current = head

previous = None

while current:#to reverse the linked list
    newnode = current.next
    current.next = previous
    previous = current
    current = newnode

head = previous

current = head
while current:
    print(current.data, end="-> ")
    current = current.next
print(None)