class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # recursive solution
        n = len(word1)
        m = len(word2)
        # def recursive(ind1, ind2):
        #     if ind1 < 0:
        #         # all characters of word1 has been matched but 
        #         # there may be characters leftover in word2
        #         # all you gotta do is insert those leftovers
        #         return ind2 + 1
        #     if ind2 < 0:
        #         # all characters of word2 has been matched but
        #         # there are leftover characters in word2
        #         # all you gotta do is delete those leftovers
        #         return ind1 + 1

        #     if word1[ind1] == word2[ind2]:
        #         return recursive(ind1 - 1, ind2 - 1)
        #     else:
        #         insert = 1 + recursive(ind1, ind2 - 1)
        #         delete = 1 + recursive(ind1 - 1, ind2)
        #         replace = 1 + recursive(ind1 - 1, ind2 - 1)
        #         return min(insert, delete, replace)

        # return recursive(n-1, m-1)
        # memoization
        # dp = [[-1] * (m) for _ in range(n)]
        # def recursive(ind1, ind2):
        #     if ind1 < 0:
        #         # all characters of word1 has been matched but 
        #         # there may be characters leftover in word2
        #         # all you gotta do is insert those leftovers
        #         return ind2 + 1
        #     if ind2 < 0:
        #         # all characters of word2 has been matched but
        #         # there are leftover characters in word2
        #         # all you gotta do is delete those leftovers
        #         return ind1 + 1
        #     if dp[ind1][ind2] != -1:
        #         return dp[ind1][ind2]

        #     if word1[ind1] == word2[ind2]:
        #         dp[ind1][ind2] = recursive(ind1 - 1, ind2 - 1)
        #         return dp[ind1][ind2]
        #     else:
        #         insert = 1 + recursive(ind1, ind2 - 1)
        #         delete = 1 + recursive(ind1 - 1, ind2)
        #         replace = 1 + recursive(ind1 - 1, ind2 - 1)
        #         dp[ind1][ind2] = min(insert, delete, replace)
        #         return dp[ind1][ind2]

        # return recursive(n-1, m-1)
        # tabulation
        # since we check if index reaches -1, we need one extra space in
        # dp table

        dp = [[0] * (m+1) for _ in range(n+1)]

        for i in range(m+1):
            dp[0][i] = i

        for j in range(n+1):
            dp[j][0] = j

        for ind1 in range(1, n+1):
            for ind2 in range(1, m+1):
                if word1[ind1 - 1] == word2[ind2 - 1]:
                    dp[ind1][ind2] = dp[ind1 - 1][ind2 - 1]
                else:
                    insert = 1 + dp[ind1][ind2 - 1]
                    delete = 1 + dp[ind1 - 1][ind2]
                    replace = 1 + dp[ind1 - 1][ind2 - 1]
                    dp[ind1][ind2] = min(insert, delete, replace)

        return dp[n][m]


        
        
