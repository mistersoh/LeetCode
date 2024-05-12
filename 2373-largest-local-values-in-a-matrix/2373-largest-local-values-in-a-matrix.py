class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        max_n = len(grid)
        n = max_n - 2
        
        answer_grid = []

        for i in range(n):
            row = []
            
            for j in range(n):
                
                sub_grid = [grid[k][j:j+3] for k in range(i,i+3)]
                max_value = max(max(sub) for sub in sub_grid)
                
                row.append(max_value)
            
            answer_grid.append(row)
        
        return answer_grid
        