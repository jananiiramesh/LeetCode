class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # recursive solution
        # let 0 and 2 be "can buy" condition
        # let 1 and 3 be "cannot buy condition"
        n = len(prices)

        # def recursive(ind, buy):
        #     if buy > 3:
        #         return 0

        #     if ind == n:
        #         return 0

        #     if buy % 2 == 0:
        #         # can buy
        #         profit = max(-prices[ind] + recursive(ind+1, buy + 1), 0 + recursive(ind+1, buy))
        #     else:
        #         profit = max(prices[ind] + recursive(ind+1, buy + 1), 0 + recursive(ind+1, buy))
        #     return profit

        # return recursive(0,0)

        # dp = [[-1] * 4 for _ in range(n)]

        # def recursive(ind, buy):
        #     if buy > 3:
        #         return 0

        #     if ind == n:
        #         return 0

        #     if dp[ind][buy] != -1:
        #         return dp[ind][buy]

        #     if buy % 2 == 0:
        #         # can buy
        #         profit = max(-prices[ind] + recursive(ind+1, buy + 1), 0 + recursive(ind+1, buy))
        #     else:
        #         profit = max(prices[ind] + recursive(ind+1, buy + 1), 0 + recursive(ind+1, buy))
        #     dp[ind][buy] = profit
        #     return dp[ind][buy]

        # return recursive(0,0)

        dp = [[0] * 5 for _ in range(n+1)]

        dp[n][0] = dp[n][1] = dp[n][2] = dp[n][3] = dp[n][4] = 0
        for i in range(n+1):
            dp[i][4] = 0

        for ind in range(n-1, -1, -1):
            for buy in range(3, -1, -1):
                profit = 0
                if buy % 2 == 0:
                    profit = max(-prices[ind] + dp[ind+1][buy + 1], 0 + dp[ind+1][buy])
                else:
                    profit = max(prices[ind] + dp[ind+1][buy + 1], 0 + dp[ind+1][buy])
                dp[ind][buy] = profit

        return dp[0][0]



            
