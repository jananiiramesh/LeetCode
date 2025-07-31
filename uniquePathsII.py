class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #recursive solution
        # m = len(obstacleGrid)
        # n = len(obstacleGrid[0])

        # def recursive(x, y):
        #     if x == m - 1 and y == n - 1:
        #         return 1

        #     if x >= m or y >= n:
        #         return 0
            
        #     if obstacleGrid[x][y] == 1:
        #         return 0

        #     right = recursive(x,y+1)
        #     down = recursive(x+1,y)

        #     return right + down

        # return recursive(0,0)

        # m = len(obstacleGrid)
        # n = len(obstacleGrid[0])

        # if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
        #     return 0

        # dp = [[-1 for _ in range(n)] for _ in range(m)]

        # def recursive(x, y):
        #     if x == m - 1 and y == n - 1:
        #         return 1

        #     if x >= m or y >= n:
        #         return 0
            
        #     if obstacleGrid[x][y] == 1:
        #         return 0

        #     if dp[x][y] != -1:
        #         return dp[x][y]

        #     right = recursive(x,y+1)
        #     down = recursive(x+1,y)

        #     dp[x][y] = right + down
        #     return dp[x][y]

        # return recursive(0,0)

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0

        dp = [[0 for _ in range(n)] for _ in range(m)]

        dp[m-1][n-1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1 , -1):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i + 1 < m:
                        dp[i][j] += dp[i+1][j]
                    if j + 1 < n:
                        dp[i][j] += dp[i][j+1]

        return dp[0][0]
