class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n=len(board)
        def get_position(s):
            r=n-1-(s-1)//n
            c=(s-1)%n  if ((n-1-r)%2==0) else (n-1-(s-1)%n)
            return r,c
        visited=set()
        queue=deque()
        queue.append((1,0))

        while queue:
            current_sq,steps=queue.popleft()
            if current_sq==n*n:
                return steps
            for i in range(1,7):
                next_sq=current_sq+i
                if next_sq>n*n:
                    continue
                r,c=get_position(next_sq)
                if board[r][c]!=-1:
                    next_sq=board[r][c]
                if next_sq not in visited:
                    visited.add(next_sq)
                    queue.append((next_sq,steps+1))
        return -1

        