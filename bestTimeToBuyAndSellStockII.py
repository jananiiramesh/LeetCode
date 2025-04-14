class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        buy_price = prices[0]
        for i in range(1,len(prices)):
            if prices[i] > buy_price:
                max_profit += prices[i] - buy_price
                buy_price = prices[i]
                continue
            if prices[i] < buy_price:
                buy_price = prices[i]
        return max_profit
