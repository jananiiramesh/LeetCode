# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return (True, 0)

            left_balanced, left_len = dfs(node.left)
            right_balanced, right_len = dfs(node.right)

            curr_balanced = (
                left_balanced and 
                right_balanced and
                abs(left_len - right_len) <= 1
            )

            curr_height = 1 + max(left_len, right_len)
            return (curr_balanced, curr_height)

        balanced,_ = dfs(root)
        return balanced

            
