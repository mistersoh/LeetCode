class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        area = 0
        directions = ((1,0),(-1,0),(0,1),(0,-1))
        grid_row = len(grid)
        grid_column = len(grid[0])

        for row_num, row in enumerate(grid):
            for col_num, col in enumerate(row):
                if col and (row_num,col_num) not in seen:
                    point = (row_num, col_num)
                    stack = [point]
                    seen.add(point)
                    curr_area = 0
                    while stack:
                        r,c = stack.pop()
                        curr_area += 1
                        for d in directions:
                            r1,c1 = r+d[0],c+d[1]
                            curr_point = (r1,c1)
                            if (0 <= r1 < grid_row and 0 <= c1 < grid_column and grid[r1][c1] and curr_point not in seen):
                                stack.append(curr_point)
                                seen.add(curr_point)

                    area = max(area, curr_area)

        return area