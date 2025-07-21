# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val:ind for ind, val in enumerate(inorder)}
        self.postorder_ind = len(postorder) - 1

        def helper(left, right):
            if left > right:
                return None

            root_val = postorder[self.postorder_ind]
            self.postorder_ind -= 1

            root = TreeNode(root_val)
            index = inorder_map[root_val]

            root.right = helper(index + 1, right)
            root.left = helper(left, index - 1)

            return root

        return helper(0, len(inorder) - 1)
