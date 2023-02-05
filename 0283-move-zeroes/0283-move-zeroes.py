class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        nums[:] = list(filter(lambda a: a != 0, nums)) + [0]*len([i for i,val in enumerate(nums) if val==0])