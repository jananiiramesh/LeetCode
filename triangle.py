class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # #recursive solution
        m = len(triangle)

        # def recursive(x, y):
        #     if x == m - 1:
        #         return triangle[x][y]

        #     path1 = recursive(x+1,y)
        #     path2 = recursive(x+1,y+1)

        #     return triangle[x][y] + min(path1, path2)

        # return recursive(0,0)
        
        #memoization
        # dp = [[-1]*(i+1) for i in range(m)]

        # def recursive(x, y):
        #     if x == m - 1:
        #         return triangle[x][y]

        #     if dp[x][y] != -1:
        #         return dp[x][y]

        #     path1 = recursive(x+1,y)
        #     path2 = recursive(x+1,y+1)

        #     dp[x][y] = triangle[x][y] + min(path1, path2)
        #     return dp[x][y]

        # return recursive(0,0)

        #tabulation
        dp = triangle[-1][:]

        for i in range(m - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])

        return dp[0]
        
