class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0

        dp = [-1]*(n+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

