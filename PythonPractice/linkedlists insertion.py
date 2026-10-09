from copyreg import dispatch_table


class data:
    def __init__(self,data):
        self.data = data
        self.next = None

data1 = data(5)
data2 = data(6)
data3 = data(7)
data4 = data(8)
data5 = data(9)
data6 = data(10)

head = data1

data1.next = data2
data2.next = data3
data3.next = data4
data4.next = data5
data5.next = data6

current = head

#inserting an element

newdata1 = data(4)
newdata1.next = head
head = newdata1

current = head

#inserting at end

newdata2 = data(11)

while current.next:
    current = current.next

current.next = newdata2

current = head

#inserting at an specific position for ex 5


newdata3 = data(5)

for i in range(4):
    current = current.next

newdata3.next = current.next
current.next = newdata3

current = head

newdata4 = data(6)
while current.data != 6:
    current = current.next

newdata4.next = current.next
current.next = newdata4

current = head

while current:
    print(current.data)
    current = current.next

#checking min value

minvalue = data1.data
current = data1.next

while current:
    if current.data < minvalue :
        minvalue = current.data

    current = current.next
print(minvalue)

#finding max value
maxvalue = data1.data
current = data1.next
while current:
    if current.data > maxvalue :
        maxvalue = current.data
    current = current.next

print(maxvalue)