class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        self.freq = 1

class Dll(object):
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0 

class LFUCache(object):
    def __init__(self, capacity):
        self.cache = {}
        self.frequency = {}
        self.capacity = capacity
        self.min_global_freq = 0

    def get(self, key):
        if key in self.cache:
            req = self.cache[key]
            old_freq = req.freq

            req.prev.next = req.next
            req.next.prev = req.prev
            self.frequency[old_freq].size -= 1 

            if old_freq == self.min_global_freq and self.frequency[old_freq].size == 0:
                self.min_global_freq += 1

            new_f = old_freq + 1
            if new_f not in self.frequency:
                self.frequency[new_f] = Dll()

            req.prev = self.frequency[new_f].head
            req.next = self.frequency[new_f].head.next
            self.frequency[new_f].head.next.prev = req
            self.frequency[new_f].head.next = req
            self.frequency[new_f].size += 1  

            req.freq = new_f
            return req.value
        else:
            return -1

    def put(self, key, value):
        if self.capacity == 0:
            return

        if key in self.cache:
            req_node = self.cache[key]
            old_freq = req_node.freq

            req_node.prev.next = req_node.next
            req_node.next.prev = req_node.prev
            self.frequency[old_freq].size -= 1  

            if old_freq == self.min_global_freq and self.frequency[old_freq].size == 0:
                self.min_global_freq += 1

            new_freq = old_freq + 1
            if new_freq not in self.frequency:
                self.frequency[new_freq] = Dll()

            req_node.prev = self.frequency[new_freq].head
            req_node.next = self.frequency[new_freq].head.next
            self.frequency[new_freq].head.next.prev = req_node
            self.frequency[new_freq].head.next = req_node
            self.frequency[new_freq].size += 1  

            req_node.freq = new_freq
            req_node.value = value
            return

        if len(self.cache) == self.capacity:
            ll = self.frequency[self.min_global_freq]
            delete = ll.tail.prev

            delete.prev.next = delete.next
            delete.next.prev = delete.prev
            ll.size -= 1  

            del self.cache[delete.key]

        newNode = Node(key, value)
        self.cache[key] = newNode
        if newNode.freq not in self.frequency:
            self.frequency[newNode.freq] = Dll()
        newNode.next = self.frequency[newNode.freq].head.next
        newNode.prev = self.frequency[newNode.freq].head
        self.frequency[newNode.freq].head.next.prev = newNode
        self.frequency[newNode.freq].head.next = newNode
        self.frequency[newNode.freq].size += 1  

        self.min_global_freq = 1
