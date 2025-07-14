# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []

        def helper(node, string):
            if node == None:
                return

            if node.left == None and node.right== None:
                string = string + f"{node.val}"
                ans.append(string[:])
                return

            helper(node.left, string + f"{node.val}->")
            helper(node.right, string + f"{node.val}->")

        helper(root, "")

        return ans
