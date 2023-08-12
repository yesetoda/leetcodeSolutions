# # # Definition for singly-linked list.
# # from typing import Optional


# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# # class Solution:
# #     def deleteDuplicates( head: Optional[ListNode]) -> Optional[ListNode]:
# #         unique = []
# #         current_node = head
# #         while current_node:
# #             if current_node.val not in unique:
# #                 unique.append(current_node.val)
# #                 current_node = current_node.next
# #             else:
# #                 prev = current_node
# #                 nxt = current_node.next
# #                 prev.next = None
# #                 current_node.next  = nxt
# #         return head
# #     head = ListNode(1)
# #     a = ListNode(2)
# #     head.next = a
# #     b = ListNode(3)
# #     a.next = b
# #     c = ListNode(4)
# #     b.next = c
# #     d = ListNode(5)
# #     c.next = d
# #     print(deleteDuplicates(head))

# from typing import Optional


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution:
#     @staticmethod
#     def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
#         unique = []
#         current_node = head
#         while current_node:
#             if current_node.val not in unique:
#                 unique.append(current_node.val)
#                 current_node = current_node.next
#             else:
#                 prev = current_node
#                 nxt = current_node.next
#                 prev.next = None
#                 current_node.next = nxt
#         return head


# # Example usage:
# head = ListNode(1)
# a = ListNode(2)
# head.next = a
# b = ListNode(2)
# a.next = b
# c = ListNode(3)
# b.next = c
# d = ListNode(3)
# c.next = d

# solution = Solution()
# result = solution.deleteDuplicates(head)

# current = result
# while current:
#     print(current.val, end=" ")
#     current = current.next
# # Output: 1 2 3

