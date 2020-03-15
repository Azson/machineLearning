class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []

        max_col = []
        for j in range(len(matrix[0])):
            max_col.append(matrix[0][j])
            for i in range(len(matrix)):
                if max_col[-1] < matrix[i][j]:
                    max_col[-1] = matrix[i][j]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == min(matrix[i]) and matrix[i][j] == max_col[j]:
                    ans.append(matrix[i][j])

        return ans


if __name__ == '__main__':
    ls = [[3,7,8],[9,11,13],[15,16,17]]
    obj = Solution()
    print(obj.luckyNumbers(ls))