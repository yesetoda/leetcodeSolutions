# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def reverse(a):
        current = a
        prev = None
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        return prev
class Solution:
    def getDecimalValue( head: ListNode) -> int:
        b = reverse(head)
        count = 0
        current = b
        out = 0
        while current:
            out+= current.val*(2**count)
            count+=1
            current = current.next
        return out
    head = ListNode(1)
    a = ListNode(0)
    head.next = a
    b = ListNode(1)
    a.next = b
    print(getDecimalValue( head))