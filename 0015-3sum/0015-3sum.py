class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        answer = []
        
        nums_len = len(nums)
        
        for i in range(nums_len-2):
            temp_array = []
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = i + 1
            r = nums_len - 1
            
            while l < r:
                
                sum_trpple = nums[i] + nums[l] + nums[r]
                
                if sum_trpple < 0:
                    l += 1
                    
                elif sum_trpple > 0:
                    r -= 1
                    
                else:
                    temp_array = [nums[i], nums[l], nums[r]]
                    
                    if temp_array not in answer:
                        
                        answer.append(temp_array)
                        
                    while l<r and nums[l] == nums[l+1]:
                        l += 1
                    while l>r and nums[r] == nums[r-1]:
                        r -= 1

                    l += 1
                    
                    r -= 1
        return answer
                