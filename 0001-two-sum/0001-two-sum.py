class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for idx, i in enumerate(nums):
            comp = target - i
            if comp in nums and nums.index(comp) != idx:
                return [idx, nums.index(comp)]