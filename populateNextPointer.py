"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        queue = deque([root])

        while queue:
            length = len(queue)

            for i in range(length):
                current = queue.popleft()
                
                if i < length - 1:
                    current.next = queue[0]
                else:
                    current.next = None

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

        return root
