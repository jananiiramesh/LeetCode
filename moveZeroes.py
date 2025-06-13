class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # one pointer to stay at place with zero
        # one pointer to find the non zero element to replace with
        i = 0
        n = len(nums)
        while i<n and nums[i] != 0 :
            i += 1
        if i>=n:
            return
        ## reached first zero position
        j = i + 1
        while j<n:
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
