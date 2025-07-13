class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_color=image[sr][sc]
        if start_color==color:
            return image
        rows,cols=len(image),len(image[0])
        queue=deque()
        queue.append((sr,sc))
        image[sr][sc]=color

        while queue:
            row,col=queue.popleft()
            directions=[(1,0),(-1,0),(0,1),(0,-1)]
            for dr,dc in directions:
                nr,nc=row+dr,col+dc
                if 0<=nr<rows and 0<=nc<cols and image[nr][nc]==start_color:
                    image[nr][nc]=color
                    queue.append((nr,nc))
        return image