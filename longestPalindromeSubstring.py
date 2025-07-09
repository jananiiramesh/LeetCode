class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        largest_pal = s[0]

        for i in range(len(s)):
            pal1 = expand(i, i)
            pal2 = expand(i, i+1)
            
            if len(pal1) > len(largest_pal):
                largest_pal = pal1
            if len(pal2) > len(largest_pal):
                largest_pal = pal2
        
        return largest_pal
