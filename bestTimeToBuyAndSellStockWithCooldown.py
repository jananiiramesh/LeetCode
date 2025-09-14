class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # recursive solution
        # 1 means can buy
        n = len(prices)
        # dp = [[-1] * 2 for _ in range(n)]

        # def recursive(ind, buy):
        #     if ind >= n:
        #         return 0

        #     if dp[ind][buy] != -1:
        #         return dp[ind][buy]

        #     if buy:
        #         profit = max(-prices[ind] + recursive(ind + 1, 0), recursive(ind + 1, 1))
        #     else:
        #         profit = max(prices[ind] + recursive(ind + 2, 1), recursive(ind + 1, 0))
        #     dp[ind][buy] = profit
        #     return dp[ind][buy]

        # return recursive(0,1)

        dp = [[0] * 2 for _ in range(n+2)]

        for ind in range(n-1, -1, -1):
            for buy in range(2):
                profit = 0
                if buy:
                    profit = max(-prices[ind] + dp[ind + 1][0], dp[ind + 1][1])
                else:
                    profit = max(prices[ind] + dp[ind + 2][1], dp[ind + 1][0])
                dp[ind][buy] = profit

        return dp[0][1]

        
