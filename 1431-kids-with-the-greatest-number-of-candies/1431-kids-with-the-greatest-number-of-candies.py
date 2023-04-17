class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        
        return ([max_candies <= (i+extraCandies) for i in candies])