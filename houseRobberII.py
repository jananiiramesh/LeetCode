class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_helper(nums):
            n = len(nums)
            if n == 0:
                return 0
            if n == 1:
                return nums[0]

            dp = [0] * n
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, n):
                dp[i] = max(nums[i] + dp[i-2], 0 + dp[i-1])

            return dp[n-1]

        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        return max(rob_helper(nums[:-1]), rob_helper(nums[1:]))

        
