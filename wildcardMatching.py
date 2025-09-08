class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # recursive solution
        n = len(s)
        m = len(p)

        dp = [[-1] * (m) for _ in range(n)]

        def recursive(ind1, ind2):
            if ind1 < 0:
                while ind2 >= 0:
                    if p[ind2] != '*':
                        return False
                    ind2 -= 1
                return True

            if ind2 < 0:
                return False

            if dp[ind1][ind2] != -1:
                return dp[ind1][ind2]

            if p[ind2] == '*':
                take = recursive(ind1 - 1, ind2)
                notTake = recursive(ind1, ind2 - 1)
                dp[ind1][ind2] = take or notTake
                return dp[ind1][ind2]

            elif p[ind2] == '?':
                dp[ind1][ind2] = recursive(ind1 - 1, ind2 - 1)
                return dp[ind1][ind2]
            else:
                if s[ind1] == p[ind2]:
                    dp[ind1][ind2] = recursive(ind1 - 1, ind2 - 1)
                    return dp[ind1][ind2]
                else:
                    dp[ind1][ind2] = False      
                    return dp[ind1][ind2]

        return recursive(n - 1, m - 1)
        
