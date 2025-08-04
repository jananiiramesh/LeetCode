from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        v = len(graph)
        colors = [0] * len(graph)

        visited = set()

        def dfs_coloring(color, node):
            colors[node] = color
            for neighbour in graph[node]:
                if colors[neighbour] == 0:
                    if not dfs_coloring(color * -1, neighbour):
                        return False
                elif colors[neighbour] == color:
                        return False
            return True

        for i in range(v):
            if colors[i] == 0:
                if not dfs_coloring(1, i):
                    return False
        return True
