class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def generate(openn, close, string):
            if len(string) == 2*n:
                res.append(string[:])
                return
            if openn < n:
                #add more opening braces
                generate(openn + 1, close, string + '(')

            if openn > close:
                #this is reached when the limit for opening is reached
                generate(openn, close + 1, string + ')')

        generate(0,0,"")
        return res
