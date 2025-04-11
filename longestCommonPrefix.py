class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #trying a non trie approach :)
        prefix = strs[0]
        for i in range(1, len(strs)):
            j = 0
            while j < min(len(strs[i]), len(prefix)): 
                if prefix[j] != strs[i][j]:
                    if j == 0:
                        prefix = ""
                        break
                    prefix = prefix[0:j]
                    break
                j += 1
            if j == len(strs[i]):
                prefix = strs[i]
        return prefix
        
