class Solution:
    def grayCode(self, n: int):
        res = [0]

        for i in range(n):
            add = 1 << i

            for j in reversed(res):
                res.append(j + add)

        return res
