# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return 
        nodes_list = []
        def preorder(node):
            if not node:
                return
            nodes_list.append(node)
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        num = len(nodes_list)
        for i in range(num - 1):
            nodes_list[i].right = nodes_list[i+1]
            nodes_list[i].left = None

        nodes_list[-1].right = None
        nodes_list[-1].left = None
        
