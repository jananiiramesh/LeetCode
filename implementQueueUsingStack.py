class MyQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        for i in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())
        data = self.stack2.pop()
        for j in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())

        return data

    def peek(self):
        """
        :rtype: int
        """
        for i in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())
        req = self.stack2[-1]
        for j in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())
        return req

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
