class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        length = len(nums)

        def generate(currindex, currlist):
            if currindex == length:
                res.append(currlist[:])
                return

            currlist.append(nums[currindex])
            generate(currindex + 1, currlist)
            currlist.pop()

            generate(currindex + 1, currlist)
        
        generate(0,[])
        return res
