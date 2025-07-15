# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        queue1 = deque()
        queue2 = deque()
        ans = []

        queue1.append(root)
        while queue1 or queue2:
            temp = []
            if queue1:
                while queue1:
                    node = queue1.popleft()
                    temp.append(node.val)
                    if node.left:
                        queue2.append(node.left)
                    if node.right:
                        queue2.append(node.right)

            else:
                while queue2:
                    node = queue2.popleft()
                    temp.append(node.val)
                    if node.left:
                        queue1.append(node.left)
                    if node.right:
                        queue1.append(node.right)

            ans.append(temp)

        return ans

