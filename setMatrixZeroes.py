class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        col_zeroes = set()
        row_zeroes = set()
        no_rows = len(matrix)
        no_cols = len(matrix[0])

        for i in range(no_rows):
            for j in range(no_cols):
                if matrix[i][j] == 0:
                    row_zeroes.add(i)
                    col_zeroes.add(j)
        
        for i in row_zeroes:
            for j in range(no_cols):
                matrix[i][j] = 0
        
        for j in col_zeroes:
            for i in range(no_rows):
                matrix[i][j] = 0


        
