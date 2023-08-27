from typing import Optional
from math import gcd

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return []
        elif not head.next:
            return head
        current = head
        while current and current.next:
            ptr = current.next
            gcd_val = gcd(current.val, ptr.val)
            gcdNode = ListNode(gcd_val)
            current.next = gcdNode
            gcdNode.next = ptr
            current = ptr
        return head

    def traverse(head):
        current = head
        while current:
            print(current.val)
            current = current.next

    a = ListNode(18)
    # b = ListNode(6)
    # a.next = b
    # c = ListNode(10)
    # b.next = c
    # d = ListNode(3)
    # c.next = d

    result = insertGreatestCommonDivisors(a)
    traverse(result)