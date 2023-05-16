class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        
        sorted_nums = sorted(set(nums))
        
        sorted_len = len(sorted_nums)
        dp = [1] * sorted_len
        start_point = 0
        
        if sorted_len == 0:
            return 0
        
        for i in range(sorted_len-1):
            
            if sorted_nums[i]+1 == sorted_nums[i+1]:
                dp[i+1] = dp[i] + dp[i+1]
                
        
        return max(dp)