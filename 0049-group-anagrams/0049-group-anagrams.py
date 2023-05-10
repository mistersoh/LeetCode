from collections import Counter
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        answer = []
        
        strs_hash = defaultdict(list)
        
        for s in (strs):
            
            s_Counter = Counter(sorted(s))
            
            strs_hash[str(s_Counter)].append(s)
        
        return (list(strs_hash.values()))
            