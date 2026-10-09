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

head = data1

data1.next = data2
data2.next = data3
data3.next = data4
data4.next = data5
data5.next = data6
data6.next = data7
data7.next = data8
data8.next = data9

current = head

while current:# modify using value
    if current.data == 9:
        current.data = 10
        break

    current = current.next

current = head
position = 1#start for modify

while current:#using a specific positon
    if position ==8:
        current.data = 9
        break

    current = current.next
    position +=1#used to parse

current = head

while current:
    print(current.data)
    current = current.next





