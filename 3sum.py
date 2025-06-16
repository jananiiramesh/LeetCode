class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            else:
                j = i + 1
                k = len(nums) - 1
                a = nums[i]
                while j < k:
                    b = nums[j]
                    c = nums[k]
                    total = a + b + c
                    if total == 0:
                        ans.append([a, b, c])
                        while j < k and nums[j] == b:
                            j += 1
                        while j < k and nums[k] == c:
                            k -= 1
                    elif total < 0:
                        j += 1
                    else:
                        k -= 1

        return ans
