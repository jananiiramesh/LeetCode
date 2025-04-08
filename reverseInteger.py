class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        length = 0
        negative = False
        if x<0:
            negative = True
            length = len(str(x)) - 1
            x = abs(x)
        else:
            length = len(str(x))
        num = 0
        i = length - 1
        while x//10 > 0:
            num = num + (x%10)*10**i
            x = x//10
            i -= 1
        num = num + (x%10)*10**i
        if negative:
            num = -(num)
        if num < -2**31 or num > 2**31 - 1:
            return 0
        return num
