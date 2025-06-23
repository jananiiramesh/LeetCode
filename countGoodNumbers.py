class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        good = 0
        power = n // 2
        mod = 10**9 + 7
        if n % 2 == 0:
            good = (pow(5, power, mod) * pow(4, power, mod)) % mod
        else:
            good = pow(5, (power + 1), mod) * pow(4, power, mod) % mod
        return good
        
