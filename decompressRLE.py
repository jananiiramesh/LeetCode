class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        j = 1
        ans = []

        while j < n:
            for _ in range(nums[i]):
                ans.append(nums[j])
            i += 2
            j += 2

        return ans
        
