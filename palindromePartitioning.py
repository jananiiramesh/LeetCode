class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []

        def palindrome(string, index, currlist):
            if index == len(string):
                result.append(currlist[:])
                return

            for i in range(index, len(string)):
                part = string[index:i+1]
                if part == part[::-1]:
                    currlist.append(part)
                    palindrome(string, i + 1, currlist)
                    currlist.pop()
        palindrome(s,0,[])
        return result
