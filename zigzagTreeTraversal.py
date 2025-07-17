# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        ans = []
        left_to_right = True

        while queue:
            lvl = []
            length = len(queue)

            for _ in range(length):
                if left_to_right:
                    node = queue.popleft()
                    lvl.append(node.val)

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

                else:
                    node = queue.pop()
                    lvl.append(node.val)

                    if node.right:
                        queue.appendleft(node.right)
                    if node.left:
                        queue.appendleft(node.left)

            left_to_right = not left_to_right
            ans.append(lvl)

        return ans
