class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows,cols=len(grid),len(grid[0])
        if rows==1 and cols==1:
            return 0
        queue=deque()
        queue.append((0,0,0,0))

        visited=set()
        visited.add((0,0,0))

        directions=[(1,0),(0,1),(-1,0),(0,-1)]

        while queue:
            row,col,steps,obs_used=queue.popleft()

            for dr,dc in directions:
                nr,nc=dr+row,dc+col

                if 0<=nr<rows and 0<=nc<cols:
                    new_obs_used=obs_used+grid[nr][nc]

                    if new_obs_used>k:
                        continue
                    if (nr,nc,new_obs_used) in visited:
                        continue
                    if nr==rows-1 and nc==cols-1:
                        return steps+1
                    visited.add((nr,nc,new_obs_used))
                    queue.append((nr,nc,steps+1,new_obs_used))

        return -1
                    
                
       