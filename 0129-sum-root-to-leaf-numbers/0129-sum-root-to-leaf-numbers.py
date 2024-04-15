# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        val = 0
        
        def dfs(node, vals):
            
            if node is None:
                return 0
            
            vals = (vals*10 + node.val)

            if node.right is None and node.left is None:
                return vals
        
            return (dfs(node.left, vals) + dfs(node.right, vals))
    
        return dfs(root, val)