class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset=set(wordList)
        if endWord not in wordset:
            return 0

        queue=deque([(beginWord,1)])
        visited=set(beginWord)
        
        while queue:
            current_word,steps=queue.popleft()

            for i in range(len(current_word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word=current_word[:i]+c+current_word[i+1:]

                    if next_word==endWord:
                        return steps+1
                    if next_word in wordset and next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word,steps+1))
        return 0
