class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []

        def combination(currindex, currlist, currsum):
            if currsum > target:
                return

            if currsum == target:
                result.append(currlist[:])
                return

            if currindex == len(candidates):
                return

            currlist.append(candidates[currindex])
            combination(currindex, currlist, currsum + candidates[currindex])
            currlist.pop()

            combination(currindex + 1, currlist, currsum)
 
        combination(0,[],0)
        return result
