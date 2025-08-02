class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #recursive solution
        m = len(grid)
        n = len(grid[0])

        # def recursive(x, y):
        #     if x == m - 1 and y == n - 1:
        #         return grid[x][y]

        #     if x >= m or y >= n:
        #         return float('inf')

        #     right = recursive(x, y+1)
        #     down = recursive(x+1, y)

        #     return grid[x][y] + min(right, down)

        # return recursive(0,0)

        #memoization
        # dp = [[-1 for _ in range(n)] for _ in range(m)]

        # def recursive(x, y):
        #     if x == m - 1 and y == n - 1:
        #         return grid[x][y]

        #     if x >= m or y >= n:
        #         return float('inf')

        #     if dp[x][y] != -1:
        #         return dp[x][y]

        #     right = recursive(x,y+1)
        #     down = recursive(x+1,y)

        #     dp[x][y] = grid[x][y] + min(right, down)
        #     return dp[x][y]

        # return recursive(0,0)

        #tabulation solution
        dp = [[0 for _ in range(n)] for _ in range(m)]

        dp[m - 1][n - 1] = grid[m - 1][n - 1]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m - 1 and j == n - 1:
                    continue
                down = dp[i + 1][j] if i + 1 < m else float('inf')
                right = dp[i][j + 1] if j + 1 < n else float('inf')
                dp[i][j] = grid[i][j] + min(down, right)

        return dp[0][0]
