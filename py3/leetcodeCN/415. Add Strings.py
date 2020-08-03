class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i = 0
        ln1, ln2 = len(num1), len(num2)
        ans = []
        f = 0
        while i < ln1 and i < ln2:
            a, b = int(num1[ln1-i-1]), int(num2[ln2-i-1])
            ans.append((a+b+f) % 10)
            f = (a+b+f) // 10
            i += 1
        while i < ln1:
            a = int(num1[ln1-i-1])
            ans.append((a + f) % 10 )
            f = (a+f) // 10
            i += 1
        while i < ln2:
            b = int(num2[ln2-i-1])
            ans.append((b + f) % 10 )
            f = (b+f) // 10    
            i += 1
        if f:
            ans.append(f)
        return ''.join(list(map(str, ans[::-1])))
