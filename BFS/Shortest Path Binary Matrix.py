class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)
        if grid[0][0]==1:
            return -1
        if n==1:
            return 1

        queue=deque([(0,0)])
        grid[0][0]=1 #Mark as visited
        path_length=1
        directions=[(1,0),(0,1),(-1,0),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1)]

        while queue:
            for _ in range(len(queue)):
                i,j=queue.popleft()
                if (i,j)==(n-1,n-1):
                    return path_length
                for di,dj in directions:
                    ni,nj=di+i,dj+j
                    if 0<=ni<n and 0<=nj<n and grid[ni][nj]==0:
                        grid[ni][nj]=1
                        queue.append((ni,nj))
            path_length+=1
        
        return -1


        