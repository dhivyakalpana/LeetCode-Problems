class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordset=set(wordList)
        if endWord not in wordset:
            return []
        #step1:BFS to build graph of word connections
        graph=defaultdict(list)
        visited=set()
        found=False
        queue=deque([beginWord])
        local_visited=set()

        while queue and not found:
            level_size=len(queue)
            local_visited.clear()
            for _ in range(level_size):
                word=queue.popleft()
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        next_word=word[:i]+c+word[i+1:]
                        if next_word in wordset and next_word not in visited:
                          if next_word==endWord:
                             found=True
                          if next_word not in local_visited:
                            queue.append(next_word)
                            local_visited.add(next_word)
                          graph[next_word].append(word)
            visited.update(local_visited)

        if not found:
            return []
        #Backtrack from endword to beginword using the graph
        res=[]
        path=[endWord]

        def backtrack(word):
            if word==beginWord:
                res.append(path[::-1])
                return
            for prev in graph[word]:
                path.append(prev)
                backtrack(prev)
                path.pop()
        backtrack(endWord)
        return res

