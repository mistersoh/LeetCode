class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        answer = [0] * len(temperatures)
        
        stack = []
        
        for num,i in enumerate(temperatures):
            
            while stack and stack[-1][1] < i:
                
                num2, i2 = stack.pop()
                
                answer[num2] = (num-num2)
            
            stack.append([num,i])
            
            
        return answer