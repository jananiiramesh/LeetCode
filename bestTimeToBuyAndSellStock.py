class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_price = prices[0]
        max_profit = 0
        for i in range(1,len(prices)):
            if prices[i] < buy_price:
                buy_price = prices[i]
                continue
            elif prices[i] > buy_price:
                profit = prices[i] - buy_price
                max_profit = max(max_profit, profit)
        return max_profit
