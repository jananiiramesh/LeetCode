"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        node_map = {}
        traverse = head

        while traverse:
            node = Node(traverse.val)
            node_map[traverse] = node
            traverse = traverse.next
        #all nodes created with mapping to original linked list parent node
        
        traverse = head
        new_head = None
        while traverse:
            if not new_head:
                new_head = node_map[traverse]
            node_map[traverse].next = node_map[traverse.next] if traverse.next else None
            node_map[traverse].random = node_map[traverse.random] if traverse.random else None
            traverse = traverse.next
        return new_head
