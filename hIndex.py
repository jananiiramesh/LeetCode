class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        h = len(citations)
        citations.sort()
        i = 0
        while i < len(citations) and citations[i] < h:
            h -= 1
            i += 1
        return h 
        
        
