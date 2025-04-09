class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        no_rows = len(matrix)
        no_cols = len(matrix[0])
        i = no_rows-1
        j = no_cols-1
        new_cols = {k: [] for k in range(0, no_cols)}
        nums = {}
        while i >= 0:
            while j >= 0:
                new_cols[j].append(matrix[i][j])
                j -= 1
            j = no_cols - 1
            i -= 1

        for row in range(no_rows):
            matrix[row] = new_cols[row]
        
