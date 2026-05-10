# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        node_list = []
        curr_node = head

        while curr_node:
            node_list.append(curr_node)
            curr_node = curr_node.next
        
        head.next = None

        for i in range(1, len(node_list)):
            node_list[i].next = node_list[i-1]
        
        return node_list[-1]

            