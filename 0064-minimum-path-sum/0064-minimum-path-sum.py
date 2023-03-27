class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]

        for j in range(1, m):
            grid[j][0] += grid[j-1][0]


        for x in range(1,m):

            for y in range(1,n):
                grid[x][y] += min(grid[x-1][y], grid[x][y-1])

        return grid[m-1][n-1]