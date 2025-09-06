class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        # def recursive(ind1, ind2):
        #     if ind2 == m:
        #         return 1
        #     if ind1 == n:
        #         return 0

        #     if s[ind1] == t[ind2]:
        #         take = recursive(ind1 + 1, ind2 + 1)
        #         notTake = recursive(ind1 + 1, ind2)
        #         return take + notTake

        #     else:
        #         return recursive(ind1 + 1, ind2)

        # return recursive(0,0)
        # def recursive(ind1, ind2):
        #     if ind2 < 0:
        #         return 1
        #     if ind1 < 0:
        #         return 0

        #     if s[ind1] == t[ind2]:
        #         take = recursive(ind1 - 1, ind2 - 1)
        #         notTake = recursive(ind1 - 1, ind2)
        #         return take + notTake

        #     return recursive(ind1 - 1, ind2)

        # return recursive(n-1, m-1)
        # dp = [[-1] * (m) for _ in range(n)]

        # def recursive(ind1, ind2):
        #     if ind2 < 0:
        #         return 1

        #     if ind1 < 0:
        #         return 0

        #     if dp[ind1][ind2] != -1:
        #         return dp[ind1][ind2]

        #     if s[ind1] == t[ind2]:
        #         take = recursive(ind1 - 1, ind2 - 1)
        #         notTake = recursive(ind1 - 1, ind2)
        #         dp[ind1][ind2] = take + notTake
        #         return dp[ind1][ind2]

        #     dp[ind1][ind2] = recursive(ind1 - 1, ind2)
        #     return dp[ind1][ind2]

        # return recursive(n-1, m-1)
        # crafting the tabulation solution
        dp = [[0] * (m+1) for _ in range(n+1)]

        for i in range(n + 1):
            dp[i][0] = 1

        for ind1 in range(1,n+1):
            for ind2 in range(1,m+1):
                if s[ind1-1] == t[ind2-1]:
                    take = dp[ind1 - 1][ind2 - 1]
                    notTake = dp[ind1 - 1][ind2]
                    dp[ind1][ind2] = take + notTake
                else:
                    dp[ind1][ind2] = dp[ind1 - 1][ind2]

        return dp[n][m]
