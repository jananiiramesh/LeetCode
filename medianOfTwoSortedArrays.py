from bisect import bisect_right

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1 and not nums2:
            return 0.0

        nums1 = nums1 or []
        nums2 = nums2 or []

        low = min(nums1[0] if nums1 else float('inf'),
                  nums2[0] if nums2 else float('inf'))
        high = max(nums1[-1] if nums1 else float('-inf'),
                   nums2[-1] if nums2 else float('-inf'))

        comb_len = len(nums1) + len(nums2)
        
        def count_less(x):
            return bisect_right(nums1, x) + bisect_right(nums2, x)

        if comb_len % 2 == 1:
            k = comb_len // 2 + 1

            while low < high:
                mid = (low + high) // 2
                if count_less(mid) < k:
                    low = mid + 1
                else:
                    high = mid

            return float(low)

        else:
            k1 = comb_len // 2
            k2 = k1 + 1

            def find(k):
                left, right = low, high
                while left < right:
                    mid = (left + right) // 2
                    if count_less(mid) < k:
                        left = mid + 1
                    else:
                        right = mid

                return left

            k1_ele = find(k1)
            k2_ele = find(k2)
            return (k1_ele + k2_ele) / 2.0
