class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # recursive solution
        # def recursive(ind1, ind2):
        #     if ind1 < 0 or ind2 < 0:
        #         return 0

        #     if text1[ind1] == text2[ind2]:
        #         return 1 + recursive(ind1 - 1, ind2 - 1)

        #     return max(recursive(ind1 - 1, ind2), recursive(ind1, ind2 - 1))

        # return recursive(len(text1) - 1, len(text2) - 1)
        # dp = [[-1] * len(text2) for _ in range(len(text1))]

        # def recursive(ind1, ind2):
        #     if ind1 < 0 or ind2 < 0:
        #         return 0
            
        #     if dp[ind1][ind2] != -1:
        #         return dp[ind1][ind2]

        #     if text1[ind1] == text2[ind2]:
        #         dp[ind1][ind2] = 1 + recursive(ind1 - 1, ind2 - 1)
        #         return dp[ind1][ind2]

        #     dp[ind1][ind2] = max(recursive(ind1 - 1, ind2), recursive(ind1, ind2 - 1))
        #     return dp[ind1][ind2]

        # return recursive(len(text1) - 1, len(text2) - 1)

        # shifting index one right
        # dp = [[-1] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        # def recursive(ind1, ind2):
        #     if ind1 == 0 or ind2 == 0:
        #         return 0
            
        #     if dp[ind1][ind2] != -1:
        #         return dp[ind1][ind2]

        #     if text1[ind1 - 1] == text2[ind2 - 1]:
        #         dp[ind1][ind2] = 1 + recursive(ind1 - 1, ind2 - 1)
        #         return dp[ind1][ind2]

        #     dp[ind1][ind2] = max(recursive(ind1 - 1, ind2), recursive(ind1, ind2 - 1))
        #     return dp[ind1][ind2]

        # return recursive(len(text1), len(text2))

        # tabulation
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for ind1 in range(1, len(text1) + 1):
            for ind2 in range(1, len(text2) + 1):
                if text1[ind1 - 1] == text2[ind2 - 1]:
                    dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]
                else:
                    dp[ind1][ind2] = max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])

        return dp[len(text1)][len(text2)]
