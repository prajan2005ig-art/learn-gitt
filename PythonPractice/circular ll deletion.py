class node:
    def __init__(self, data):
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

while current.next != head:#delete at first
    current = current.next

head = head.next
current.next = head

current = head

while current.next.next != head:#delete at last
    current = current.next

current.next = head

current = head

for i in range(0):#delete at a specific position
    current = current.next

current.next = current.next.next
current = head

while current.data != 4:#delete at a data after a specific data
    current = current.next
current.next = current.next.next

current = head

key = 2

while True:
    if current.data == key:
        print("Key found")
        break
    current = current.next

    if current.data == head:
        break

current = head

count = 0

while True:
    count += 1
    current = current.next
    if current == head:
        break

print("the count is:",count)

current = head


while True:
    print(current.data)
    current = current.next

    if current == head:
        break

