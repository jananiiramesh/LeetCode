# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        postorder = []

        def helper(root):
            if root == None:
                return

            helper(root.left)
            helper(root.right)
            postorder.append(root.val)

        helper(root)
        return postorder
