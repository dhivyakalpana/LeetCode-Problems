class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0

        visited=set()
        queue=deque()
        queue.append((0,0))

        while queue:
            current_sum,steps=queue.popleft()
            for coin in coins:
                next_sum=coin+current_sum
                if next_sum==amount:
                    return steps+1
                if next_sum < amount and next_sum not in visited:
                    visited.add(next_sum)
                    queue.append((next_sum,steps+1))
        return -1
