"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        hash_map = {}

        queue = deque([node])
        while queue:
            temp_var = queue.popleft()
            if temp_var not in hash_map:
                #true only for first node
                new_node = Node(temp_var.val)
                hash_map[temp_var] = new_node
            
            for neighbor in temp_var.neighbors:
                if neighbor not in hash_map:
                    hash_map[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                hash_map[temp_var].neighbors.append(hash_map[neighbor])

        return hash_map[node]
