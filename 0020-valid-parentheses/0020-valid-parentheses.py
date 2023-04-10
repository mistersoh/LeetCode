class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for i in s:
            if i == '(' or i == "{" or i == "[":
                stack.append(i)
            
            else:
                if not stack or (i == ")" and stack[-1] != "(") or (i == "}" and stack[-1] != "{") or (i == "]" and stack[-1] != "["):
                        return False
                stack.pop()
            
        if stack:
            return False
        
        return True
        