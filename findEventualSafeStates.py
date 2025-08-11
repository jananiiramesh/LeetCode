from collections import defaultdict, deque
from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        answer = []
        reverse_graph = defaultdict(list)
        V = len(graph)
        in_degree = [0]*V
        for i in range(V):
            for neighbour in graph[i]:
                reverse_graph[neighbour].append(i)
                in_degree[i] += 1

        queue = deque([i for i in range(V) if in_degree[i] == 0])

        while queue:
            node = queue.popleft()
            answer.append(node)

            for neighbour in reverse_graph[node]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)

        return sorted(answer)
