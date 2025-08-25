class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        # def recursive(ind, target):
        #     if target == 0:
        #         return 1
        #     if ind < 0:
        #         return 0

        #     notTake = recursive(ind - 1, target)
        #     if target - coins[ind] >= 0:
        #         take = recursive(ind, target - coins[ind])
        #     else:
        #         take = 0

        #     return take + notTake

        # return recursive(n-1, amount)

        #now to memoize it
        # dp = [[-1] * (amount + 1) for _ in range(n)]
        # def recursive(ind, target):
        #     if target == 0:
        #         return 1
        #     if ind < 0:
        #         return 0

        #     if dp[ind][target] != -1:
        #         return dp[ind][target]

        #     notTake = recursive(ind - 1, target)
        #     if target - coins[ind] >= 0:
        #         take = recursive(ind, target - coins[ind])
        #     else:
        #         take = 0

        #     dp[ind][target] = take + notTake
        #     return dp[ind][target]

        # return recursive(n-1, amount)

        # finally to tabulate it
        dp = [[0] * (amount + 1) for _ in range(n)]
        
        # base case
        # at any value of ind, if target is 0, that will have 1
        for i in range(n):
            dp[i][0] = 1

        for t in range(0, amount + 1):
            if t % coins[0] == 0:
                dp[0][t] = 1

        for ind in range(1, n):
            for target in range(1, amount + 1):
                notTake = dp[ind - 1][target]
                if target - coins[ind] >= 0:
                    take = dp[ind][target - coins[ind]]
                else:
                    take = 0

                dp[ind][target] = notTake + take

        return dp[n-1][amount]
        
        
