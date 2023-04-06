class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        directions = ((1,0),(0,1),(-1,0),(0,-1))
        grid_row = len(grid)
        grid_column = len(grid[0])
        num_island = []
        
        
        for row_num in range(1,grid_row-1):
            
            for col_num in range(1,grid_column-1):
                
                if grid[row_num][col_num] == 0 and (row_num,col_num) not in seen:
                    point = (row_num,col_num)
                    
                    stack = [point]
                    seen.add(point)
                    curr_area = 0
                    not_island = True
                    while stack:
                        r,c = stack.pop()
                        curr_area += 1
                        for d in directions:
                            r1, c1 = r + d[0], c + d[1]

                            curr_point = (r1,c1)

                            if not (0 <= r1 < grid_row and 0 <= c1 < grid_column):
                                not_island = False

                            elif not grid[r1][c1] and curr_point not in seen:
                                stack.append(curr_point)
                                seen.add(curr_point)

                            
                    if not_island:
                        num_island.append(curr_area)

                    
        return len(num_island) - num_island.count(0)