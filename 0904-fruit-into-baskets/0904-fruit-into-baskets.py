class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        better = 0
        nums = Counter()
        
        for r in range(len(fruits)):
            nums[fruits[r]] += 1
            
            while len(nums) > 2:
                nums[fruits[l]] -= 1
                if nums[fruits[l]] == 0:
                    nums.pop(fruits[l])
                    
                l += 1
                
            better = max(better, r-l+1)
        return better