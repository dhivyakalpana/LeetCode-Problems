class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n=len(arr)

        queue=deque([start])
        visited=set()

        while queue:
            i=queue.popleft()

            if i<0 or i>=n or i in visited:
                continue
            
            if arr[i]==0:
                return True

            visited.add(i)

            queue.append(i+arr[i])
            queue.append(i-arr[i])
        
        return False
        