class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.ls = [0]*maxSize
        self.now = 0


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.now < len(self.ls):
            self.ls[self.now] = x
            self.now += 1


    def pop(self):
        """
        :rtype: int
        """
        if self.now > 0:
            self.now -= 1
            return self.ls[self.now]
        return -1


    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        for i in range(min(k, len(self.ls))):
            self.ls[i] += val



# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)