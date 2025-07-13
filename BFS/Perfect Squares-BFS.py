class Solution:
    def numSquares(self, n: int) -> int:
        squares=[i*i for i in range(1,int(n**0.5)+1)]

        queue=deque([n])
        level=0

        while queue:
            level+=1
            for _ in range(len(queue)):
                current=queue.popleft()

                for sq in squares:
                    next_val=current-sq
                    if next_val==0:
                        return level
                    if next_val>0:
                        queue.append(next_val)
                    else:
                        break
        return level