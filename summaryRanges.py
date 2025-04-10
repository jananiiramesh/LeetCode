class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []

        ranges = []
        interval_start = False
        more_than_one = False
        interval_beg = nums[0]

        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i] + 1:
                if not interval_start:
                    interval_start = True
                    interval_beg = nums[i]
                more_than_one = True
            else:
                if interval_start and more_than_one:
                    rstr = "{}->{}".format(interval_beg, nums[i])
                    ranges.append(rstr)
                else:
                    ranges.append("{}".format(nums[i]))
                interval_start = False
                more_than_one = False
                interval_beg = nums[i + 1]

        if interval_start and more_than_one:
            rstr = "{}->{}".format(interval_beg, nums[-1])
            ranges.append(rstr)
        else:
            ranges.append("{}".format(nums[-1]))

        return ranges
