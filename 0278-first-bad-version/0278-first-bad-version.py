# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        l = 1
        r = n
        
        
        
        while l <= r:
            
            midpoint = (l+r)//2
            
            if isBadVersion(midpoint):
                r = midpoint -1
                
            else:
                l = midpoint+1
                
        return l