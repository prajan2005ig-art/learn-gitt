class node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

data1 = node(1)
data2 = node(2)
data3 = node(3)
data4 = node(4)

head = data1

data1.next = data2
data2.prev = data1

data2.next = data3
data3.prev = data2

data3.next = data4
data4.prev = data3

newdata1 = node(0)#inserting at first
newdata1.next = head
head.prev = newdata1
head = newdata1


current = head

newdata2 = node(5)

while current.next:#inserting at last
    current = current.next

current.next = newdata2
newdata2.prev = current
current = head

newdata3 = node(6)#inserting at specific point
for i in range(4):
    current = current.next

newdata3.next = current.next
newdata3.prev = current.prev
current.next.prev = newdata3
current.next = newdata3

current = head

while current:
    print(current.data)
    current = current.next






