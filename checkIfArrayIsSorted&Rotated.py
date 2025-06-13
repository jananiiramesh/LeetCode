class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        breaks = 0
        n = len(nums)
        for i in range(n):
            if nums[i] <= nums[(i+1)%n]:
                continue
            else:
                breaks += 1
                if breaks > 1:
                    return False
        return True
