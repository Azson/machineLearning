class MinStack(object):
    #时间换空间就对了
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.ls = []
        self.mn = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.ls.append(x)
        tmp = min(self.mn[-1], x) if len(self.mn) else x
        self.mn.append(tmp)

    def pop(self):
        """
        :rtype: None
        """
        self.ls.pop(-1)
        self.mn.pop(-1)

    def top(self):
        """
        :rtype: int
        """
        return self.ls[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.mn[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()