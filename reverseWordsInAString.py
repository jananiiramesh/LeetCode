class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        list_words = s.split()
        if len(list_words) == 1:
            return s
        rstr = list_words[len(list_words)-1]
        i = len(list_words) - 2
        while i >= 0:
            rstr = rstr + " " + list_words[i]
            i -= 1
        return rstr

        
        
