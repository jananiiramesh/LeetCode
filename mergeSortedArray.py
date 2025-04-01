class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        k = m+n-1
        if len(nums2) == 0:
            return #empty second list
        while (i>=0 and j>=0):
            if nums1[i] >= nums2[j]: #greater element in nums1 it self
                nums1[k], nums1[i] = nums1[i], nums1[k]
                i = i - 1
            else:
                nums1[k] = nums2[j]
                j = j - 1
            k = k - 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        