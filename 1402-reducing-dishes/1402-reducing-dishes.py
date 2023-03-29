class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        max_satis = 0
        suffixsum = 0

        satisfaction.sort()

        for i in range(len(satisfaction)-1,-1,-1):
            suffixsum += satisfaction[i]
            if suffixsum > 0:
                max_satis += suffixsum


        return max_satis