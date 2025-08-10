class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:

        i1, j = x, y
        i2 = x + (k-1)
        j_limit = y + (k-1)

        while i2 > i1:
            while j <= j_limit:
                grid[i1][j], grid[i2][j] = grid[i2][j], grid[i1][j]
                j += 1
            j = y
            i1 += 1
            i2 -= 1

        return grid
