class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # recursive solution
        n = len(coins)
        if amount == 0:
            return 0
        # def coin(ind, target):
        #     if ind == 0:
        #         if target % coins[ind] == 0:
        #             return target // coins[ind]
        #         else:
        #             return 1e9

        #     notTake = 0 + coin(ind - 1, target)
        #     take = float('inf')
        #     if coins[ind] <= target:
        #         take = 1 + coin(ind, target - coins[ind])

        #     return min(notTake, take)

        # ans = coin(n-1, amount)
        # return -1 if ans >= 1e9 else ans

        # memoization solution
        # dp = [[-1] * (amount + 1) for _ in range(n)]
        # def coin(ind, target):
        #     if ind == 0:
        #         if target % coins[ind] == 0:
        #             return target // coins[ind]
        #         else:
        #             return 1e9

        #     if dp[ind][target] != -1:
        #         return dp[ind][target]

        #     notTake = 0 + coin(ind - 1, target)
        #     take = float('inf')
        #     if coins[ind] <= target:
        #         take = 1 + coin(ind, target - coins[ind])

        #     dp[ind][target] = min(notTake, take)
        #     return dp[ind][target]

        # ans = coin(n-1, amount)
        # return -1 if ans >= 1e9 else ans

        # tabulation
        dp = [[0] * (amount + 1) for _ in range(n)]
        # at index 0, dp[0][target] would be equal to target // coins[0] if
        # its divisible
        dp[0][0] = 0
        for i in range(1, amount + 1):
            if i % coins[0] == 0:
                dp[0][i] = i // coins[0]
            else:
                dp[0][i] = 1e9

        for index in range(1,n):
            for target in range(amount + 1):
                notTake = 0 + dp[index - 1][target]
                take = 1e9
                if coins[index] <= target:
                    take = 1 + dp[index][target - coins[index]]
                dp[index][target] = min(notTake, take)

        ans = dp[n-1][amount]
        return -1 if ans >= 1e9 else ans
        
