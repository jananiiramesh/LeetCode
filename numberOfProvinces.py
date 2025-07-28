class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected:
            return 0

        n = len(isConnected)
        provinces = 0
        visited = set()

        def dfs_helper(node):
            visited.add(node)
            
            for i in range(n):
                if isConnected[node][i] == 1 and i not in visited:
                    dfs_helper(i)

        for j in range(n):
            if j not in visited:
                provinces += 1
                dfs_helper(j)

        return provinces
