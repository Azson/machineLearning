class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """
        used = set()

        for i in range(n):

            if leftChild[i] in used or rightChild[i] in used:
                return False
            if leftChild[i] != -1:
                used.add(leftChild[i])
            if rightChild[i] != -1:
                used.add(rightChild[i])

        if len(used) != n-1:
            return False

        return True

if __name__ == '__main__':
    n = 4
    leftChild = [1, -1, 3, -1]
    rightChild = [2, 3, -1, -1]
    obj = Solution()
    print(obj.validateBinaryTreeNodes(n, leftChild, rightChild))