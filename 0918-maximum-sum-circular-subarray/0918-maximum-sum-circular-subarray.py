import math

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        array_sum = 0
        curr_max = -math.inf
        max_so_far = -math.inf
        curr_min = math.inf
        min_so_far = math.inf

        # Concept of Kadane's Algorithm
        for i in range(len(nums)):

            # Compute sum of complete array
            array_sum += nums[i]
            # print("array sum", array_sum)

            # Kadane's Algorithm to find Maximum subarray sum.
            curr_max = max(curr_max + nums[i], nums[i])
            # print("curr_max", curr_max)
            max_so_far = max(max_so_far, curr_max)
            # print("max_so_far", max_so_far)

            # Kadane's Algorithm to find Minimum subarray sum.
            curr_min = min(curr_min + nums[i], nums[i])
            # print("curr_min", curr_min)
            min_so_far = min(min_so_far, curr_min)
            # print("min_so_far", min_so_far)
            
        if (array_sum == min_so_far):
            return max_so_far
        
        return max(max_so_far, array_sum - min_so_far)