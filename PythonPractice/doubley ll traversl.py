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

while current.next:
   current = current.next

#current = head

while current:
    print(current.data)
    current = current.prev
