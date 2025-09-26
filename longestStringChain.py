class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        # recursive solution
        n = len(words)
        # dp = [[-1] * (n+1) for _ in range(n)]

        def mismatch(prev, curr):
            if len(words[curr]) - len(words[prev]) != 1:
                return True

            i = j = 0
            mismatches = 0
            while i < len(words[prev]) and j < len(words[curr]):
                if words[prev][i] == words[curr][j]:
                    i += 1
                else:
                    mismatches += 1
                    if mismatches > 1:
                        return True
                j += 1

            return False

        # def recursive(ind, prev_ind):
        #     if ind == n:
        #         return 0

        #     if dp[ind][prev_ind+1] != -1:
        #         return dp[ind][prev_ind+1]

        #     notTake = recursive(ind+1, prev_ind)
        #     take = 0
        #     if prev_ind == -1 or not mismatch(prev_ind, ind):
        #         take = 1 + recursive(ind+1, ind)

        #     dp[ind][prev_ind+1] = max(notTake, take)
        #     return dp[ind][prev_ind+1]

        # return recursive(0, -1)

        dp = [[0] * (n+1) for _ in range(n+1)]

        for ind in range(n-1, -1, -1):
            for prev_ind in range(ind-1, -2, -1):
                notTake = dp[ind+1][prev_ind+1]
                take = 0
                if prev_ind == -1 or not mismatch(prev_ind, ind):
                    take = 1 + dp[ind+1][ind+1]
                
                dp[ind][prev_ind+1] = max(take, notTake)

        return dp[0][0] 


        
