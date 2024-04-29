# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        path = []
        
        def to_next(path, node):
            
            if node:
                to_next(path,node.left)
                path.append(node.val)
                to_next(path,node.right)
        
        to_next(path, root)
        return path