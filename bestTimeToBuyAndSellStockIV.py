class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # let even numbers be "can buy condition"
        # recursive solution
        n = len(prices)
        # dp = [[-1] * 2*k for _ in range(n)]

        # def recursive(ind, buy):
        #     if buy >= 2*k:
        #         return 0

        #     if ind == n:
        #         return 0

        #     if dp[ind][buy] != -1:
        #         return dp[ind][buy]

        #     if buy % 2 == 0:
        #         profit = max(-prices[ind] + recursive(ind+1, buy+1), 0 + recursive(ind+1, buy))
        #     else:
        #         profit = max(prices[ind] + recursive(ind+1, buy+1), 0 + recursive(ind+1, buy))

        #     dp[ind][buy] = profit
        #     return dp[ind][buy]

        # return recursive(0,0)
        dp = [[0] * (2*k + 1) for _ in range(n+1)]

        for ind in range(n-1, -1, -1):
            for buy in range(2*k-1, -1, -1):
                profit = 0
                if buy % 2 == 0:
                    profit = max(-prices[ind] + dp[ind+1][buy+1], 0 + dp[ind+1][buy])
                else:
                    profit = max(prices[ind] + dp[ind+1][buy+1], 0 + dp[ind+1][buy])
                dp[ind][buy] = profit

        return dp[0][0]


        
