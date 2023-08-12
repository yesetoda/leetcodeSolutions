# # Definition for singly-linked list.
# from typing import Optional


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# def reverse(a):
#         current = a
#         prev = None
#         while current:
#             nxt = current.next
#             current.next = prev
#             prev = current
#             current = nxt
#         return prev
# class Solution:
#     def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         b = reverse(head)
#         print(b)
#         current = b
#         while n!=1:
#             current = current.next
#             n ==1
#         nxt = current.next.next
#         current.next = nxt
#         a = reverse(b)
#         return a
#     head = ListNode(1)
#     a = ListNode(0)
#     head.next = a
#     b = ListNode(1)
#     a.next = b
#     c = ListNode(1)
#     b.next = c
#     d = ListNode(1)
#     c.next = d
#     print(removeNthFromEnd(head,1))




from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def reverse(a):
        current = a
        prev = None
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        return prev

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        b = self.reverse(head)
        current = b
        
        if n > 1:
            while n != 1 and current:
                current = current.next
                n -= 1
            if current and current.next:
                current.next = current.next.next
        elif n == 1:
            if current and current.next:
                current.next = current.next.next
            else:
                b = None
        a = self.reverse(b)
        return a


# Example usage:
head = ListNode(1)
a = ListNode(2)
head.next = a
b = ListNode(3)
a.next = b
c = ListNode(4)
b.next = c
d = ListNode(5)
c.next = d

solution = Solution()
result = solution.removeNthFromEnd(head, 2)
current = result
while current:
    print(current.val, end=" ")
    current = current.next
# Output: 0 1 1 1