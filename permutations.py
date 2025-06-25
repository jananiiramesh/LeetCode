class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        used = [0]*len(nums)

        def permutations(currlist):
            if len(currlist) == len(nums):
                result.append(currlist[:])

            for i in range(len(used)):
                if used[i] == 1:
                    continue

                currlist.append(nums[i])
                used[i] = 1
                permutations(currlist)

                currlist.pop()
                used[i] = 0
 
        permutations([])
        return result
