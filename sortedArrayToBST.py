# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def convert(arr):
            length = len(arr)
            if length == 1:
                return TreeNode(arr[0])

            i = length // 2
            root = TreeNode(arr[i])
            root.left = convert(arr[:i])
            root.right = convert(arr[i+1:]) if i+1 < length else None
            return root

        return convert(nums)
        
