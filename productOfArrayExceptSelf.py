class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        prefix = [0]*n
        postfix = [0]*n
        output = [0]*n

        for i in range(n):
            if i == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = nums[i]*prefix[i-1]

        for j in range(n-1,-1,-1):
            if j == n - 1:
                postfix[j] = nums[j]
            else:
                postfix[j] = nums[j] * postfix[j+1]

        for k in range(n):
            ## output[k] = prefix[k-1] * postfix[k+1]
            if k == 0:
                output[k] = 1 * postfix[k+1]
            elif k == n - 1:
                output[k] = prefix[k-1] * 1
            else:
                output[k] = prefix[k-1] * postfix[k+1]

        return output
