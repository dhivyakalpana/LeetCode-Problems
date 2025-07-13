class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        flat=[num for row in board for num in row]
        if sorted(flat)!=[0,1,2,3,4,5]:
            raise valueError("Invalid board input: must contain digits 0 through exactly once.")
        
        start=''.join(str(num) for num in flat)
        target='123450'

        neighbors={
            0:[1,3],
            1:[0,2,4],
            2:[1,5],
            3:[0,4],
            4:[1,3,5],
            5:[2,4]
        }

        visited=set()
        visited.add(start)

        queue=deque([(start,0)])

        while queue:
            state,moves=queue.popleft()

            if state==target:
                return moves

            zero_index=state.index('0')

            for neighbor in neighbors[zero_index]:
                new_state=list(state)
                new_state[zero_index],new_state[neighbor]=new_state[neighbor],new_state[zero_index]
                new_state_str=''.join(new_state)

                if new_state_str not in visited:
                    visited.add(new_state_str)
                    queue.append((new_state_str,moves+1))
        return -1
        