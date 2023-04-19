# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        self.paths = 0
        
        def dfs(node):
            
            if node is None:
                return (0,0)
            
            left = dfs(node.left)[0] 
            right = dfs(node.right)[1] 
            self.paths = max(self.paths, left, right)
            
            return (right + 1, left + 1)
            
        dfs(root)
        return self.paths
                
            