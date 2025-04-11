#any Negative number is by default False. 0 will by default by True. All you gotta do is reverse the number
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        if x==0:
            return True
        initial = x
        rev_int = 0
        while x>0:
            add = x % 10
            rev_int = rev_int * 10 + add
            x = x//10
        
        return rev_int == initial
