class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        spiral_matrix = []
        length = len(matrix)
        width = len(matrix[0])
        area = length * width

        go_right = True
        go_down = False
        go_left = False
        go_up = False

        top = 0
        bottom = length - 1
        left = 0
        right = width - 1

        while len(spiral_matrix) < area:
            if go_right:
                for i in range(left, right + 1):
                    spiral_matrix.append(matrix[top][i])
                top += 1
                go_right = False
                go_down = True

            elif go_down:
                for i in range(top, bottom + 1):
                    spiral_matrix.append(matrix[i][right])
                right -= 1
                go_down = False
                go_left = True

            elif go_left:
                for i in range(right, left - 1, -1):
                    spiral_matrix.append(matrix[bottom][i])
                bottom -= 1
                go_left = False
                go_up = True

            elif go_up:
                for i in range(bottom, top - 1, -1):
                    spiral_matrix.append(matrix[i][left])
                left += 1
                go_up = False
                go_right = True

        return spiral_matrix
