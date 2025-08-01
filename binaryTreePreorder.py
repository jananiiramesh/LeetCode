# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        preorder = []
        def helper(root):
            if root == None:
                return

            preorder.append(root.val)
            helper(root.left)
            helper(root.right)

        helper(root)
        return preorder
