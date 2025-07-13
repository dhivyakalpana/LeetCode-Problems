class Solution:
    def racecar(self, target: int) -> int:
        if target==0:
            return 0
        
        queue=deque([(0,0,1)])
        seen=set([(0,1)])

        while queue:
            moves,position,speed=queue.popleft()
            next_position=position+speed
            next_speed=speed*2

            if next_position==target:
                return moves+1
            
            if 0<=next_position<2*target and (next_position,next_speed) not in seen:
                seen.add((next_position,next_speed))
                queue.append((moves+1,next_position,next_speed))
            
            rev_speed=-1 if speed>0 else 1

            if (position,rev_speed) not in seen:
                seen.add((position,rev_speed))
                queue.append((moves+1,position,rev_speed))
        
        return -1
            
