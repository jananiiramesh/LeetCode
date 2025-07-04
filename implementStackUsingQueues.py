from collections import deque
class MyStack(object):

    def __init__(self):
        self.queue = deque()
        self.start = -1
        self.end = -1

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.append(x)

    def pop(self):
        """
        :rtype: int
        """
        for i in range(len(self.queue) - 1):
            self.push(self.queue.popleft())
        return self.queue.popleft()

    def top(self):
        """
        :rtype: int
        """
        return self.queue[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
