class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        points = {num: -1 for num in nums1}
        stack = []

        for num in nums2:
            while stack and num > stack[-1]:
                prev = stack.pop()
                if prev in points:
                    points[prev] = num

            stack.append(num)

        return [points[num] for num in nums1]
