# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 1, 2, last element
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        
        fast = slow = head

        while n:
            fast= fast.next
            n -= 1

        if not fast:
            return slow.next

        while fast.next:
            fast = fast.next
            slow = slow.next
        

        slow.next = slow.next.next if slow.next else None
        
        return head
        


