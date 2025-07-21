# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(root,1)])
        max_len = 1
        set_first = False

        while queue:
            length = len(queue)
            for _ in range(length):
                node, ind = queue.popleft()
                if not set_first:
                    first_ind = ind
                    last_ind = first_ind
                    set_first = True
                else:
                    last_ind = ind
                if node.left:
                    queue.append((node.left, 2*ind))
                if node.right:
                    queue.append((node.right, 2*ind + 1))
            max_len = max(max_len, last_ind - first_ind + 1)
            set_first = False

        return max_len
