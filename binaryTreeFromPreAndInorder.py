# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val:ind for ind, val in enumerate(inorder)}
        self.prefix_ind = 0

        def helper(left, right):
            if left > right:
                return None

            root_val = preorder[self.prefix_ind]
            self.prefix_ind += 1

            root = TreeNode(root_val)
            index = inorder_map[root_val]

            root.left = helper(left, index - 1)
            root.right = helper(index + 1, right)

            return root

        return helper(0, len(inorder) - 1)
