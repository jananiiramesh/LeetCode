class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return -1
        index = -1
        i, j = 0, 0
        continuation = False
        while i<len(haystack) and j<len(needle):
            if continuation:
                if haystack[i] == needle[j]:
                    i += 1
                    j += 1
                else:
                    continuation = False
                    i = index + 1
                    j = 0
                continue
            if haystack[i] == needle[j]:
                continuation = True
                index = i
                i+=1
                j+=1
            else:
                i+=1
        if i == len(haystack) and j != len(needle):
            return -1
        else:
            return index
