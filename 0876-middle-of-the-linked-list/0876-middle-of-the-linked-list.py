# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def getCount(self, node: Optional[ListNode]):
            if not node:
                return 0
            else:
                return 1 + getCount(self, node.next)
        full_len = getCount(self, head)

        # print(full_len)
        
        middle_len = full_len // 2
        
        temp_m = head
        while middle_len != 0:
            temp_m = temp_m.next
            # print(temp_m)
            middle_len -= 1
            
        return temp_m