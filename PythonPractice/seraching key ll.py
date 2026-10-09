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

head = head.next#delete at first
current = head

while current.next.next is not None:#delete at last
    current = current.next

current.next = None

current = head


position = 3

for i in range(position - 2):
    current = current.next

current.next = current.next.next

key = 2
found = False

current = head

while current:#to find wheather an element exists
    if current.data == key:
        print("key found")
        found = True
        break#should not use else when using break
    current = current.next

if found == False:#use true or false in this case
    print("key not found")

current = head
while current:
    print(current.data)
    current = current.next


