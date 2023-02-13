# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # if list1 is None:
        #     return list2
        # if list2 is None:
        #     return list1
        
        s = t = ListNode()
        
        while list1 and list2:
            if list1.val <= list2.val:
                c = list1
                list1 = list1.next
                
            else:
                c = list2
                list2 = list2.next
                
            t.next = c
            t = t.next
        
        t.next = list1 or list2
        
        return s.next