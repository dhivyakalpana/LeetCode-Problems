class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue=deque([root])
        result=[]
        left_to_right=True

        while queue:
            level_size=len(queue)
            current_level=deque()

            for _ in range(level_size):
                node=queue.popleft()
                

                if left_to_right:
                    current_level.append((node.val))
                else:
                    current_level.appendleft((node.val))

                if node.left:
                    queue.append((node.left))
                if node.right:
                    queue.append((node.right))

            result.append(list(current_level))
            left_to_right= not left_to_right
            
        return result

        
        