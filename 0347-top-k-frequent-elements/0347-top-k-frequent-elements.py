from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        most_common_num = (Counter(nums).most_common(k))
        
        return [num[0] for num in most_common_num]