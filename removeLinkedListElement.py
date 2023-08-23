# Definition for singly-linked list.
from typing import Optional


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# # class Solution:
# def removeElements( head: Optional[ListNode], val: int) -> Optional[ListNode]:
#         if  head == None:
#             return None
#         elif head.val == val:
#             prev = head
#             head = head.next
#             print(prev.val,head.val)
#             prev.next = None
#             return head
#         else:
#             prev = head
#             current = prev.next
#             while current != None:
#                 if current.val != val:
#                     prev = prev.next
#                     current = current.next
#                 else:
#                     print("values is found")
#                     prev.next = current.next
#                     # removeElements(head,val)
                    # return head

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    if head is None:
        return None
    elif head.val == val:
        head = head.next
        return removeElements(head, val)
    else:
        prev = head
        current = prev.next
        while current is not None:
            if current.val != val:
                prev = prev.next
                current = current.next
            else:
                prev.next = current.next
                return removeElements(head, val)
        return head


def Traverse(head):
    if head is None:
        print([])
    else:
        current = head
        while current is not None:
            print(" ==> ", current.val, end="")
            current = current.next
        print()


a = ListNode(7)
a.next = ListNode(7)
a.next.next = ListNode(0)
a.next.next.next = ListNode(7)

Traverse(a)
a = removeElements(a, 7)
Traverse(a)
# a.next.next.next.next = ListNode(7)
# a.next.next.next.next.next = ListNode(7)
# a.next.next.next.next.next.next = ListNode(7)
Traverse(a)
removeElements(a,7)
Traverse(a)