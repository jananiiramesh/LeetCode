class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        viewed = {}
        for i in range(len(nums)):
            if nums[i] not in viewed:
                viewed[nums[i]] = []
            viewed[nums[i]].append(i)
        
        for key in viewed:
            if len(viewed[key]) > 1:
                check_this = viewed[key]
                for j in range(1, len(check_this)):
                    if abs(check_this[j] - check_this[j-1]) <= k:
                        return True
        return False

        
