class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # def recursive(ind, currsum):
        #     if ind < 0:
        #         if currsum == 0:
        #             return 1
        #         else:
        #             return 0

        #     plus = recursive(ind - 1, currsum - nums[ind])
        #     minus = recursive(ind - 1, currsum + nums[ind])

        #     return plus + minus

        # return recursive(n-1, target)

        # trying to memoize it
        s = sum(nums)
        # dp = [[float('inf')] * (2*s + 1) for _ in range(n)]
        # def recursive(ind, currsum):
        #     if ind < 0:
        #         if currsum == target:
        #             return 1
        #         else:
        #             return 0

        #     if dp[ind][currsum] != float('inf'):
        #         return dp[ind][currsum]

        #     plus = recursive(ind - 1, currsum + nums[ind])
        #     minus = recursive(ind - 1, currsum - nums[ind])

        #     dp[ind][currsum] = plus + minus
        #     return dp[ind][currsum]

        # return recursive(n-1, 0)

        # tabulation
        offset = s
        dp = [[0] * (2*s + 1) for _ in range(n)]

        if nums[0] == 0:
            dp[0][offset] = 2  
        else:
            dp[0][nums[0] + offset] = 1
            dp[0][-nums[0] + offset] = 1

        for i in range(1, n):
            for summ in range(-s, s+1):
                if dp[i-1][summ + offset] > 0:
                    if -s <= summ + nums[i] <= s:
                        dp[i][summ + nums[i] + offset] += dp[i-1][summ + offset]
                    if -s <= summ - nums[i] <= s:
                        dp[i][summ - nums[i] + offset] += dp[i-1][summ + offset]

        return 0 if abs(target) > s else dp[n-1][target + offset]


            
