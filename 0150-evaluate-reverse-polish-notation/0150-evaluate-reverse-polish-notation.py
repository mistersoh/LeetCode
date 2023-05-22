class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        num_stack = []
        
        for t in tokens:
            
            if t not in "+=-*/":
                num_stack.append(int(t))
            else:
                num_1 = num_stack.pop()
                num_2 = num_stack.pop()
                
                if t == "+":
                
                    calc = num_1 + num_2
                    num_stack.append(calc)
                
                elif t == "-":
                    
                    calc = num_2 - num_1
                    num_stack.append(calc)
                
                elif t == "*":
                    calc = num_1 * num_2
                    num_stack.append(calc)
                
                elif t == "/":
                    calc = int(float(num_2)/float(num_1))
                    num_stack.append(calc)
            
        return num_stack.pop()