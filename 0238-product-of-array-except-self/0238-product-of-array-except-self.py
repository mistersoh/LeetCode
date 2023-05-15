class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        outputs_1 = [1] * len(nums)
        outputs_2 = [1] * len(nums)
        output = [0] * len(nums)
        
        
        for i in range(1, len(nums)):
            
            outputs_1[i] = outputs_1[i-1] * nums[i-1]
            
        for i in reversed(range(0, len(nums)-1)):
            outputs_2[i] = outputs_2[i+1]*nums[i+1]
        
        for i in range(len(nums)):
            output[i] = outputs_1[i] * outputs_2[i]
            
        return output