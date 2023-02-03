class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ans = [""] * numRows
        goback = True
        index = 0
        
        for char in s:
            # Add current char to row
            ans[index] += char
            
            # if index reaches to first of end row, change direction
            if index == 0 or index == numRows - 1:
                goback = not goback
                
            if goback:
                index -= 1
                
            else:
                index += 1
                
        return "".join(ans)