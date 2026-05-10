# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# [0 1 2 3]
# [0 -> 1 -> None ]
from copy import copy
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        new_head = self.reverse(head, head.next)
        head.next = None

        return new_head

    
    def reverse(self, curr, next):
        if next is None:
            return curr
        
        temp = next
        next = next.next
        temp.next = curr
        curr = temp

        return self.reverse(curr, next)





        