class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()

        def subset(currindex, currlist):
            if currindex == len(nums):
                result.append(currlist[:])
                return
            
            currlist.append(nums[currindex])
            subset(currindex + 1, currlist)
            currlist.pop()

            subset(currindex + 1, currlist)
            
        subset(0,[])
        result.sort()
        i = 0
        while i < len(result) - 1:
            if result[i] == result[i + 1]:
                result.pop(i + 1)
            else:
                i += 1
        
        return result
