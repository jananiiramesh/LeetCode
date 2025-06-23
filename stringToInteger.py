class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()
        if not s:
            return 0
        negative = False
        num = 0
        if s[0] == '-' or s[0] == '+':
            negative = s[0] == '-'
            i = 1
        else:
            i = 0
        startFound = False
        while i < len(s):
            if not s[i].isdigit():
                break
            else:
                if s[i] == '0' and not startFound:
                    i += 1
                    continue
                elif s[i] != '0' and not startFound:
                    startFound = True

                if startFound:
                    num = (num * 10) + int(s[i])
            i += 1

        if negative:
            num = - num
        
        if num < -2**31:
            return -2**31

        if num > 2**31 - 1:
            return 2**31 - 1

        return num
