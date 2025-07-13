class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:

        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        rows,cols=len(forest),len(forest[0])
        trees=[]

        for i in range(rows):
            for j in range(cols):
                if forest[i][j]>1:
                    trees.append((forest[i][j],i,j))
        trees.sort()
        
        def bfs(sr,sc,dr,dc):
            if sr==dr and sc==dc:
                return 0

            queue=deque([(sr,sc,0)])
            visited=set()
            visited.add((sr,sc))

            while queue:
                row,col,steps=queue.popleft()
                for dcr,dcc in directions:
                    nr,nc=row+dcr,col+dcc
                    if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited and forest[nr][nc]!=0:
                        if(nr,nc)==(dr,dc):
                            return steps+1
                        visited.add((nr,nc))
                        queue.append((nr,nc,steps+1))
            return -1

        current_row,current_col=0,0
        total_steps=0

        for height,tree_row,tree_col in trees:
            steps=bfs(current_row,current_col,tree_row,tree_col)
            if steps==-1:
                return -1
            total_steps+=steps

            forest[tree_row][tree_col]=1 #cut the tree

            current_row,current_col=tree_row,tree_col

        return total_steps



                