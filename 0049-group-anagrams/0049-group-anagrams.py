from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        strs_hash = defaultdict(list)
        
        for s in (strs):
            
            s_sorted = str(sorted(s))
            
            strs_hash[s_sorted].append(s)
        
        return (list(strs_hash.values()))
            