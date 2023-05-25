class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        if len(piles) == h:
            return max(piles)
        
        
        l, r = 1, max(piles)
        
        while l <= r:
            
            sum_eats = 0
            
            mid = (r + l) // 2
            
            for i in piles:
                
                sum_eats += i//mid
                
                if i % mid != 0:
                    sum_eats += 1
                
            if sum_eats <= h:
                r = mid - 1
                
            else:
                l = mid + 1
                
        return l