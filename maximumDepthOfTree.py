# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        maxDepth = 1

        def depth(node, length):
            nonlocal maxDepth
            if node == None:
                return 
                
            if node.left == None and node.right == None:
                maxDepth = max(maxDepth, length)
                return

            depth(node.left, length + 1)
            depth(node.right, length + 1)

        depth(root,1)
        return maxDepth
