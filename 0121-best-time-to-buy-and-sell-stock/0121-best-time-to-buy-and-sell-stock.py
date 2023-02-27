class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn, mx = prices[0], 0               
        for p in prices: 
                                           
            if p < mn: 
                mn = p
            elif p > mx + mn:
                mx = p - mn
        return mx   