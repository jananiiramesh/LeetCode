class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numbers = set(nums)
        longest_length = 0

        for num in numbers:
            if num - 1 not in numbers:
                current = num
                streak = 1
            
                while current + 1 in numbers:
                    current += 1
                    streak += 1

                longest_length = max(longest_length, streak)

        return longest_length
