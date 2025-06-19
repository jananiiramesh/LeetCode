class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        total_water = 0
        prefix_max = [0]*n
        suffix_max = [0]*n
        for i in range(n):
            if i == 0:
                prefix_max[i] = height[i]
            else:
                prefix_max[i] = max(prefix_max[i-1], height[i])
        for i in range(n-1,-1,-1):
            if i == n-1:
                suffix_max[i] = height[i]
            else:
                suffix_max[i] = max(suffix_max[i+1], height[i])
        for i in range(n):
            leftmax = prefix_max[i]
            rightmax = suffix_max[i]
            if height[i] < leftmax and height[i] < rightmax:
                total_water += min(leftmax, rightmax) - height[i]
        
        return total_water
