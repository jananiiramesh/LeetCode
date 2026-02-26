# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # at any point, you can either move right or left
        # path HAS to end at the leaf
        if not root:
            return False

        def recursion(node, currSum):
            if not node.left and not node.right:
                # leaf node
                return currSum + node.val == targetSum

            leftPath = recursion(node.left, currSum + node.val) if node.left else False
            rightPath = recursion(node.right, currSum + node.val) if node.right else False
            return leftPath or rightPath

        return recursion(root, 0)
