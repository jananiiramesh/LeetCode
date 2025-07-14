# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        nodes = []
        ans = []

        def helper(node, col, row):
            if node == None:
                return

            helper(node.left, col-1, row+1)
            nodes.append((col,row,node.val))
            helper(node.right, col+1, row+1)

        helper(root, 0, 0)

        prev_col = float('inf')

        nodes.sort()
        for col, row, val in nodes:
            if col != prev_col:
                ans.append([])
                prev_col = col
            ans[-1].append(val)

        return ans
        
