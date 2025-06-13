class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        i = 0
        max_window, curr_window = 0,0
        while i<n:
            if nums[i] == 1:
                curr_window += 1
            else:
                max_window = max(max_window, curr_window)
                curr_window = 0
            i += 1
        return max(max_window, curr_window)
