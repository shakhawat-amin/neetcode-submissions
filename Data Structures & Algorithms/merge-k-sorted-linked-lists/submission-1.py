# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        output = None
        for l in lists:
            output = self.mergeList(output, l)

        return output
    
    def mergeList(self, list1, list2):
        if not list1:
            return list2
        if not list2: 
            return list1
        
        dummy_node = ListNode(0)
        new_list = dummy_node

        while list1 and list2:
            if list1.val < list2.val:
                new_list.next = list1
                list1 = list1.next
            else:
                new_list.next = list2
                list2 = list2.next
            
            new_list = new_list.next
            
        
        new_list.next = list1 if not list2 else list2
        
        return dummy_node.next
