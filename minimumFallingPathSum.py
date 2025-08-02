class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # #recursive soln
        n = len(matrix)
        # def recursive(x, y):
        #     if y < 0 or y >= n:
        #         return float('inf')

        #     if x == n - 1:
        #         return matrix[x][y]

        #     path1 = recursive(x+1,y-1)
        #     path2 = recursive(x+1,y)
        #     path3 = recursive(x+1,y+1)

        #     return matrix[x][y] + min(path1, path2, path3)

        # return min(recursive(0, y) for y in range(n))

        #memoization
        # dp = [[-1 for _ in range(n)] for _ in range(n)]

        # def recursive(x, y):
        #     if y < 0 or y >= n:
        #         return float('inf')

        #     if x == n - 1:
        #         return matrix[x][y]

        #     if dp[x][y] != -1:
        #         return dp[x][y]

        #     path1 = recursive(x+1,y-1)
        #     path2 = recursive(x+1,y)
        #     path3 = recursive(x+1,y+1)

        #     dp[x][y] = matrix[x][y] + min(path1, path2, path3)
        #     return dp[x][y]

        # return min(recursive(0, y) for y in range(n))
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for j in range(n):
            dp[n-1][j] = matrix[n-1][j]

        for i in range(n-2, -1, -1):
            for j in range(n):
                path1 = dp[i+1][j-1] if j-1 >= 0 else float('inf')
                path2 = dp[i+1][j]
                path3 = dp[i+1][j+1] if j+1 < n else float('inf')

                dp[i][j] = matrix[i][j] + min(path1, path2, path3)

        return min(dp[0])


