class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary = bin(n)[2:]
        binary = str(binary)
        count = 0
        for num in binary:
            if num == '1':
                count += 1
        return count
        
