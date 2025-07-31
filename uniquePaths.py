class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # ##exploring recursive solution first

        # def recursive(x, y):

        #     if x == m - 1 and y == n - 1:
        #         return 1

        #     if x >= m or y >= n:
        #         return 0

        #     right = recursive(x+1,y)
        #     down = recursive(x,y+1)

        #     return right + down

        # return recursive(0,0)

        ##now explore memoization
        # dp = [[-1 for _ in range(n)] for _ in range(m)]

        # def recursive(x, y):
        #     if x == m - 1 and y == n - 1:
        #         return 1

        #     if x >= m or y >= n:
        #         return 0

        #     if dp[x][y] != -1:
        #         return dp[x][y]

        #     right_paths = recursive(x+1,y)
        #     down_paths = recursive(x,y+1)

        #     dp[x][y] = right_paths + down_paths
        #     return dp[x][y]

        # return recursive(0,0)

        #now tabulation
        dp = [[0 for _ in range(n)] for _ in range(m)]

        dp[m-1][n-1] = 1 #base case in recursion converted here

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i+1 < m:
                    dp[i][j] += dp[i+1][j]
                if j+1 < n:
                    dp[i][j] += dp[i][j+1]

        return dp[0][0]
