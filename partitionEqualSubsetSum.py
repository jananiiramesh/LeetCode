class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # #recursive solution
        total = sum(nums)

        if total % 2 == 1:
            return False

        target_sum = total // 2
        length = len(nums)

        # def recursive(ind, curr_sum):
        #     if curr_sum == target_sum:
        #         return True

        #     if curr_sum > target_sum or ind == length:
        #         return False

        #     #take element in partition 1
        #     left_tree = recursive(ind + 1, curr_sum + nums[ind])
        #     #take element in partition 2 (which we're not keeping track of)
        #     right_tree = recursive(ind + 1, curr_sum)

        #     return (left_tree or right_tree)

        # return recursive(0, 0)

        #memoization solution
        #state variables = ind, currsum
        #ind can range from 0 to len(nums)
        #currsum can range from 0 to targetsum (total // 2)
        # dp = [[-1] * (target_sum + 1) for _ in range(length + 1)]

        # def recursive(ind, currsum):
        #     if currsum == target_sum:
        #         return True

        #     if currsum > target_sum or ind == length:
        #         return False

        #     if dp[ind][currsum] != -1:
        #         return dp[ind][currsum]

        #     left_tree = recursive(ind + 1, currsum + nums[ind])
        #     right_tree = recursive(ind + 1, currsum)

        #     dp[ind][currsum] = left_tree or right_tree
        #     return dp[ind][currsum]

        # return recursive(0,0)

        #tabulation technique

        dp = [[False] * (target_sum + 1) for _ in range(length+1)]

        # no matter what index we are at, sum of 0 is always possible
        for i in range(length+1):
            dp[i][0] = True

        for i in range(1, length+1):
            for s in range(1, target_sum+1):
                if s >= nums[i - 1]:
                    dp[i][s] = dp[i-1][s] or dp[i-1][s - nums[i-1]]
                else:
                    dp[i][s] = dp[i-1][s]

        return dp[length][target_sum]
