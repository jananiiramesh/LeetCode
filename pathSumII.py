# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        path = []
        def recursion(node, currSum, currPath):
            if not node:
                return 

            currPath.append(node.val)
            currSum += node.val

            if not node.left and not node.right:
                # leaf node
                if currSum == targetSum:
                    path.append(currPath[:])

            if node.left:
                leftPath = recursion(node.left, currSum, currPath)
            if node.right:
                right = recursion(node.right, currSum, currPath)

            currPath.pop()

        recursion(root, 0, [])
        return path
