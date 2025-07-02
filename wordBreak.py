class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_set = set(wordDict)
        memo = {}

        def search(i):
            if i == len(s):
                return True

            if i in memo:
                return memo[i]

            for word in word_set:
                n = len(word)
                if i+n <= len(s) and s[i:i+n] == word:
                    if search(i+n):
                        memo[i] = True
                        return True
            memo[i] = False
            return False

        return search(0)
