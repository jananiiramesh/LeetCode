class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        one_thirds = []
        nums.sort()
        threshold = len(nums) // 3
        if len(nums) == 1:
            return nums
        count = 1
        candidate = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == candidate:
                count += 1
            else:
                if count > threshold:
                    one_thirds.append(candidate)
                candidate = nums[i]
                count = 1
        if count > threshold:
            one_thirds.append(candidate)
        return one_thirds
        


        
