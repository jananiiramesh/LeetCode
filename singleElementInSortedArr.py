class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        while (low < high):
            mid = (low + high) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid - 1]:
                ##indicates the single element is before mid
                high = mid - 2
            elif nums[mid] == nums[mid + 1]:
                ##indicates the single element is after mid + 1
                low = mid + 2
            else:
                return nums[mid]

        return nums[low]
