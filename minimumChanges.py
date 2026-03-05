class Solution:
    def minOperations(self, s: str) -> int:
        # string will either start with 0 or 1, no other choice
        # if it starts with 0 or 1, check the indexes
        s0 = 0
        l = len(s)

        # think string should start from 0
        for i in range(l):
            if i%2 == 0 and s[i] != '0':
                s0 += 1
            elif i%2 == 1 and s[i] != '1':
                s0 += 1

        s1 = 0
        for j in range(l):
            if j%2 == 0 and s[j] != '1':
                s1 += 1
            elif j%2 == 1 and s[j] != '0':
                s1 += 1

        return min(s0, s1)
