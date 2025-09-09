class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = float('-inf')
        pre, suff = 1, 1
        n = len(nums)
        for i in range(n):
            if pre == 0:
                pre = 1
            if suff == 0:
                suff = 1
            pre *= nums[i]
            suff *= nums[n-i-1]
            max_prod = max(max_prod, max(pre, suff))

        return max_prod
        
