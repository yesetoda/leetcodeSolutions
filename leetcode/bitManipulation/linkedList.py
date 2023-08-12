class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
a = Node("A")
b = Node("B")
a.next = b
c = Node("C")
b.next = c
d = Node("D")
c.next = d
current = a
while current:
    print(current.data)
    current = current.next
    
print("def")
def reverse(a):
    current = a
    prev = None
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev
x = reverse(a)
print("reversed")
current = x
while current:
    print(current.data)
    current = current.next