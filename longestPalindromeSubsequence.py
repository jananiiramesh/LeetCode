class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s1 = s
        s2 = s[::-1]

        dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        for ind1 in range(1, len(s1) + 1):
            for ind2 in range(1, len(s2) + 1):
                if s1[ind1 - 1] == s2[ind2 - 1]:
                    dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]
                else:
                    dp[ind1][ind2] = max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])

        return dp[len(s1)][len(s2)]
