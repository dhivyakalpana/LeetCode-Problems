class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead=set(deadends)

        if '0000' in dead:
            return -1
        
        queue=deque([('0000',0)])
        visited=set()
        visited.add('0000')

        while queue:
            current_state,steps=queue.popleft()

            if current_state==target:
                return steps
            
            for i in range(4):
                digit=int(current_state[i])
                for move in [-1,1]:
                    new_digit=(digit+move)%10
                    new_combo=current_state[:i]+str(new_digit)+current_state[i+1:]
                    if new_combo not in dead and new_combo not in visited:
                        visited.add(new_combo)
                        queue.append((new_combo,steps+1))
                        
        return -1


