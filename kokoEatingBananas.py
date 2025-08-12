import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # min speed can be eating 1 banana per hours
        # max speed can be max(piles)
        if h < len(piles):
            return 0
        
        # naive approach
        # start with 1 banana per hous, check if the pile satisfies it
        # if not increment k, and retry
        # not at all efficient - O(max(piles)*len(piles))
        lower, upper = 1, max(piles)
        result = upper

        while lower <= upper:
            mid = (lower + upper) // 2
            total = sum(math.ceil(piles[i]/mid) for i in range(len(piles)))
            if total <= h:
                result = mid
                upper = mid - 1
            else:
                lower = mid + 1

        return result
        # time complexity - O(nlog(max(piles)))


        
