class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ## more efficient soln
        nums_new = [0]*len(nums)
        pos = 0
        neg = 1
        for num in nums:
            if num>0:
                nums_new[pos] = num
                pos += 2
            else:
                nums_new[neg] = num
                neg += 2
        return nums_new
        
