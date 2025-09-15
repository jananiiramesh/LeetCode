class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # recursive function
        n = len(nums)
        # dp = [[-1] * (n+1) for _ in range(n)]

        # def recursive(ind, prev_ind):
        #     if ind == n:
        #         return 0

        #     if dp[ind][prev_ind] != -1:
        #         return dp[ind][prev_ind]

        #     notTake = recursive(ind+1, prev_ind)
        #     take = 0
        #     if prev_ind == -1 or nums[ind] > nums[prev_ind]:
        #         take = 1 + recursive(ind+1, ind)

        #     dp[ind][prev_ind] = max(notTake, take)
        #     return dp[ind][prev_ind]

        # return recursive(0, -1)

        dp = [[0] * (n+1) for _ in range(n+1)]

        for ind in range(n-1, -1, -1):
            for prev_ind in range(ind - 1, -2, -1):
                notTake = dp[ind+1][prev_ind + 1]
                take = 0
                if prev_ind == -1 or nums[ind] > nums[prev_ind]:
                    take = 1 + dp[ind+1][ind+1]

                dp[ind][prev_ind+1] = max(take, notTake) 
        return dp[0][0]  
