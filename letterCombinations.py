class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
            
        mapping = {
            '2' : ['a','b','c'],
            '3' : ['d','e','f'],
            '4' : ['g','h','i'],
            '5' : ['j','k','l'],
            '6' : ['m','n','o'],
            '7' : ['p','q','r','s'],
            '8' : ['t','u','v'],
            '9' : ['w','x','y','z']
        }

        res = []

        def combinations(currindex, currstring):
            if currindex == len(digits):
                res.append(currstring[:])
                return

            for i in range(len(mapping[digits[currindex]])):
                combinations(currindex + 1, currstring + mapping[digits[currindex]][i])

        combinations(0,"")
        return res
