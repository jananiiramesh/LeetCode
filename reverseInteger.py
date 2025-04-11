class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        if x<0:
            negative = True
            x = abs(x)
        num = 0
        while x > 0:
            add = x % 10
            num = num * 10 + add
            x = x//10
        if negative:
            num = -(num)
        if num < -2**31 or num > 2**31 - 1:
            return 0
        return num
