class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s_2 = ''.join(filter(str.isalnum,s.lower()))
            
        return s_2 == s_2[::-1]