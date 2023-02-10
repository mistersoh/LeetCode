class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        dirs = ((1,0), (0,1), (-1,0), (0,-1))
        visited = set()
        point = image[sr][sc]
        
        def dfs(r,c):
            if (r,c) in visited:
                return
            visited.add((r,c))
            for d in dirs:
                x, y = r+d[0], c+d[1]
                if 0 <= x < rows and 0 <= y < cols and image[x][y] == point:
                    image[x][y] = color
                    dfs(x,y)

        if point != color:
            image[sr][sc] = color
            dfs(sr,sc)

        return image