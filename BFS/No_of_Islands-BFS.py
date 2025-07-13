class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows,cols=len(grid),len(grid[0])
        islands=0

        def bfs(r,c):
            queue=deque()
            queue.append((r,c))
            grid[r][c]='0' #mark visited

            while queue:
                row,col=queue.popleft()
                directions=[(1,0),(-1,0),(0,1),(0,-1)]
                for dr,dc in directions:
                    nr,nc=row+dr,col+dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]=='1':
                        grid[nr][nc]='0'
                        queue.append((nr,nc))
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1':
                    islands+=1
                    bfs(r,c)
        return islands




        