class Solution:
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_counter = Counter(s1)
        
        l = 0
        r = len(s1)
        
        s2_len = len(s2)
        
        while l<s2_len+1:
        
            if s1_counter == Counter(s2[l:r]):
                return True
            
            l+=1
            r+=1
        
        return False
            
            