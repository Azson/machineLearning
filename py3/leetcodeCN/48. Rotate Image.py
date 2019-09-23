class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        def recur_rotate(l, n, matrix):
            if n <= 1:
                return
            for x in range(n):
                matrix[l][l+x], matrix[x][l+n-1] = matrix[x][l+n-1], matrix[l][l+x]
            for x in range(n):
                matrix[l][l + x], matrix[l + n - 1][x] = matrix[l + n - 1][x], matrix[l][l + x]

            recur_rotate(l+1, n-2, matrix)
        recur_rotate(0, len(matrix), matrix)

        return matrix
