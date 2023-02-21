class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        size = len(nums)
        
        left, right = 0, size // 2
        
        while left < right:
            
            pair_index = left + ( right - left ) // 2
            
            if nums[2*pair_index] != nums[2*pair_index+1]:
                right = pair_index
            
            else:
                left = pair_index + 1
        
        return nums[2*left]