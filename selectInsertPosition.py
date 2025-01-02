from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Check if the target exists in the list
        if nums.count(target) != 0:
            # If found, return the index where the target is located
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
        else:
            # If the target is not found, find the insertion position
            for i in range(len(nums)):
                if nums[i] > target:
                    return i
            # If target is greater than all elements, return the length of the list
            return len(nums)