class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n = len(s)
        m = len(p)

        dp = [[-1] * (m+1) for _ in range(n+1)]

        def recursive(ind1, ind2):
            if ind1 < 0:
                # string over, check if pattern is over
                while ind2 >= 0:
                    if p[ind2] != '*':
                        return False
                    ind2 -= 2
                return True

            if ind2 < 0:
                return False

            if dp[ind1][ind2] != -1:
                return dp[ind1][ind2]

            if p[ind2] == '*':
                notTake = recursive(ind1, ind2-2)

                take = False
                if ind2 > 0 and (p[ind2 - 1] == s[ind1] or p[ind2 - 1] == '.'):
                    take = recursive(ind1 - 1, ind2)

                dp[ind1][ind2] = notTake or take
                return dp[ind1][ind2]

            elif p[ind2] == ".":
                dp[ind1][ind2] = recursive(ind1 - 1, ind2 - 1)
                return dp[ind1][ind2]

            else:
                if p[ind2] == s[ind1]:
                    dp[ind1][ind2] = recursive(ind1 - 1, ind2 - 1)
                    return dp[ind1][ind2]
                else:
                    dp[ind1][ind2] = False
                    return dp[ind1][ind2]

        return recursive(n - 1, m - 1)
