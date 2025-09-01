class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        delete = 0

        for ind1 in range(1, len(word1) + 1):
            for ind2 in range(1, len(word2) + 1):
                if word1[ind1 - 1] == word2[ind2 - 1]:
                    dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]
                else:
                    dp[ind1][ind2] = max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])

        lcs = dp[len(word1)][len(word2)]
        delete += len(word1) - lcs
        delete += len(word2) - lcs
        return delete
        
