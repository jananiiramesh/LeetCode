class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.capacity = capacity
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            req = self.cache[key]
            req.prev.next = req.next
            req.next.prev = req.prev
            req.prev = self.head
            req.next = self.head.next
            self.head.next.prev = req
            self.head.next = req
            return req.value

        else:
            return -1
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            req_node = self.cache[key]
            req_node.value = value
            req_node.prev.next = req_node.next
            req_node.next.prev = req_node.prev
            req_node.prev = self.head
            req_node.next = self.head.next
            self.head.next.prev = req_node
            self.head.next = req_node
            return

        if len(self.cache) == self.capacity:
            delete = self.tail.prev
            #need to remove this node and put it in the starting
            delete.prev.next = delete.next
            delete.next.prev = delete.prev
            delete.prev = self.head
            delete.next = self.head.next
            #now there are two elements that point to head
            self.head.next.prev = delete
            self.head.next = delete

            #need to modify cache key
            del self.cache[delete.key]

            delete.key = key
            delete.value = value

            self.cache[key] = delete
        else:
            newNode = Node(key, value)
            newNode.next = self.head.next
            self.head.next.prev = newNode
            self.head.next = newNode
            newNode.prev = self.head

            self.cache[key] = newNode

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
