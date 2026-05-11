# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head.next if head else None
        slow = head

        while fast and slow:
            if fast == slow:
                return True
            
            fast = fast.next.next if fast.next else None
            slow = slow.next
        
        return False