class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # # # recursive solution to find the length lcs
        n = len(str1)
        m = len(str2)

        # # def recursive(ind1, ind2):
        # #     if ind1 < 0 or ind2 < 0:
        # #         return 0

        # #     if str1[ind1] == str2[ind2]:
        # #         return 1 + recursive(ind1 - 1, ind2 - 1)
            
        # #     else:
        # #         return max(recursive(ind1 - 1, ind2), recursive(ind1, ind2 - 1))
        # # memoization
        # # dp = [[-1] * (m+1) for _ in range(n+1)]

        # # def recursive(ind1, ind2):
        # #     if ind1 < 0 or ind2 < 0:
        # #         return 0

        # #     if dp[ind1][ind2] != -1:
        # #         return dp[ind1][ind2]

        # #     if str1[ind1] == str2[ind2]:
        # #         return 1 + recursive(ind1 - 1, ind2 - 1)

        # #     return max(recursive(ind1 - 1, ind2), recursive(ind1, ind2 - 1))

        # # return recursive(n,m)
        dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

        for ind1 in range(1, len(str1) + 1):
            for ind2 in range(1, len(str2) + 1):
                if str1[ind1 - 1] == str2[ind2 - 1]:
                    dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]
                else:
                    dp[ind1][ind2] = max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])

        lcs = dp[len(str1)][len(str2)]

        subseq = []
        i, j = n, m
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                subseq.append(str1[i-1])
                i -= 1
                j -= 1
            
            elif dp[i-1][j] > dp[i][j-1]:
                subseq.append(str1[i-1])
                i -= 1

            else:
                subseq.append(str2[j-1])
                j -= 1

        while i > 0:
            subseq.append(str1[i - 1])
            i -= 1
        while j > 0:
            subseq.append(str2[j - 1])
            j -= 1

        return "".join(reversed(subseq))

    








        
