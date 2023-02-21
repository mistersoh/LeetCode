class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return([k for k,v in list(Counter(nums).items()) if v == 1][0])