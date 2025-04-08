class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        hashmap = {i:[] for i in range(1, numRows + 1)}
        current_row = 1
        downward = True
        for i in range(len(s)):
            hashmap[current_row].append(s[i])
            if current_row == numRows:
                downward = False
            elif current_row == 1:
                downward = True
            current_row += 1 if downward else -1
        zig = ''.join([''.join(hashmap[row]) for row in range(1, numRows + 1)])
        return zig
