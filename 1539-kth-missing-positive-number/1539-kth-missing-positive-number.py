class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        i = 0
        
        while True:
            
            if k == 0:
                return i
            
            i+=1
            if i in arr:
                continue
            else:
                k -= 1
            