class StockSpanner(object):

    def __init__(self):
        self.stack = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        if not self.stack:
            count = 1
            self.stack.append((price, 1))
        else:
            count = 1
            while self.stack and self.stack[-1][0] <= price:
                val, count_prev = self.stack.pop()
                count += count_prev
            self.stack.append((price, count))

        return count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
