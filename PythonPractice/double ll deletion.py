class node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

data1 = node(1)
data2 = node(2)
data3 = node(3)
data4 = node(4)
data5 = node(5)

head = data1

data1.next = data2
data2.prev = data1

data2.next = data3
data3.prev = data2

data3.next = data4
data4.prev = data3

data4.next = data5
data5.prev = data4

current = head

head = head.next# delete at first
head.prev = None

current = head

while current.next:#delete at last
    current = current.next

current = current.prev
current.next = None

current = head

for i in range(2):#delete at specific  location
    current = current.next
if current.next:
    current.next.prev = current.prev
if current.prev:
    current.prev.next = current.next

current = head


while current:
    print(current.data)
    current = current.next

