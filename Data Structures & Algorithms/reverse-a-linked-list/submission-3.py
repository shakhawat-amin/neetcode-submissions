# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# [0 1 2]
# prev -> 1, curr = 2, next None
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        prev = None
        curr = head
        next_val = head.next

        while curr:
            curr.next = prev
            prev = curr
            curr = next_val
            next_val = curr.next if curr else None

        return prev



