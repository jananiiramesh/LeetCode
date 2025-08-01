from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        pattern_map = defaultdict(list)
        L = len(beginWord)

        for word in wordList:
            for i in range(L):
                pattern = word[:i] + '*' + word[i+1:]
                pattern_map[pattern].append(word)

        queue = deque([(beginWord, 1)])
        visited = set([beginWord])

        while queue:
            curr_word, level = queue.popleft()
            for i in range(L):
                pattern = curr_word[:i] + '*' + curr_word[i+1:]

                for neighbour in pattern_map[pattern]:
                    if neighbour == endWord:
                        return level + 1
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append((neighbour, level + 1))

        return 0
