class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i, j = 0, 0
        children = 0
        # i maintains g and j maintains s
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                children += 1
                i += 1
            j += 1
        return children
        
