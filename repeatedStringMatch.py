class Solution(object):
    def repeatedStringMatch(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        count = 1
        temp = a

        while len(temp) < len(b):
            temp += a
            count += 1

        if b in temp:
            return count

        temp += a
        count += 1

        if b in temp:
            return count

        return -1
