# from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # string_dict = defaultdict(int)
        
        if len(s) != len(t):
            return False
        
        return sorted(t) == sorted(s)