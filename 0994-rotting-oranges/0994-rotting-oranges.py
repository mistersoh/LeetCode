class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        h, w = len(grid), len(grid[0])

        all_fresh = 0

        all_rotten = []

        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    all_fresh += 1
                if grid[i][j] == 2:
                    all_rotten.append((j,i,0))

        traversal_queue = deque(all_rotten)

        moves = 0

        while traversal_queue:
            x, y, time = traversal_queue.popleft()

            for dirs in directions:
                nx, ny = x+dirs[0],y+dirs[1]
                if 0<=nx<w and 0<=ny<h and grid[ny][nx] == 1:
                    all_fresh -= 1
                    grid[ny][nx] = -1

                    moves = time + 1

                    traversal_queue.append( (nx, ny, time + 1) )

        if all_fresh == 0:
            return moves

        else:
            return -1