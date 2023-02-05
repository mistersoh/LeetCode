class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        l = 0
        r = len(p)
        ans = []
        p_counter = Counter(p)
        
        while r < len(s)+1:
            if Counter(s[l:r]) == p_counter:
                ans.append(l)
                
            l += 1
            r += 1
            
        return ans