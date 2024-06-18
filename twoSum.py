class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #nums.sort()
        l=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j]==target-nums[i]:
                    l.append(i)
                    l.append(j)
                    return l
        return []