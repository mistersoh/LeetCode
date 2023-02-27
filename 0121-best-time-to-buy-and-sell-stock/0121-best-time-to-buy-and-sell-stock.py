class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0,1
        diff = 0

        while right < len(prices):

            if prices[right]  > prices[left]:
                diff = max(diff, prices[right] - prices[left])
            else:
                left = right

            right += 1

        return diff