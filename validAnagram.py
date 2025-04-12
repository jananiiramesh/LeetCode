class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        letters_s = {}
        letters_t = {}
        for letter in s:
            if letter not in letters_s:
                letters_s[letter] = 0
            letters_s[letter] += 1
        for letter in t:
            if letter not in letters_t:
                letters_t[letter] = 0
            letters_t[letter] += 1
            
        return letters_s == letters_t
        
