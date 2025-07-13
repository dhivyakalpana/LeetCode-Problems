class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]

        graph=defaultdict(set)
        degree=[0]*n
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
            degree[u]+=1
            degree[v]+=1   
        leaves=deque(i for i in range(n) if degree[i]==1)
        remaining_nodes=n

        while remaining_nodes>2:
            leaves_count=len(leaves)
            remaining_nodes-=leaves_count
            for _ in range(leaves_count):
                leaf=leaves.popleft()

                for nei in graph[leaf]:
                    degree[nei]-=1
                
                    if degree[nei]==1:
                        leaves.append(nei)
        
        return list(leaves)

                



    

    