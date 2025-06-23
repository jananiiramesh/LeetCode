class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = ""
        nums = []
        def factorial(num):
            if num == 1 or num == 0:
                return 1

            fact = num * factorial(num-1)
            return fact

        length = n
        for i in range(1,n+1):
            nums.append(i)

        k -= 1
        for i in range(n):
            fact = factorial(len(nums)-1)
            index = k//fact
            k = k%fact
            res += str(nums[index])
            nums.pop(index)

        return res
