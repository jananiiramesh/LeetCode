class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()

        def dfs_helper(x, y, region):
            if x < 0 or x >= m or y < 0 or y >= n:
                return True

            if board[x][y] != 'O' or (x, y) in visited:
                return False

            visited.add((x,y))
            region.append((x, y))

            touches_border = False
            for dx, dy in directions:
                if dfs_helper(x + dx, y + dy, region):
                    touches_border = True

            return touches_border

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i,j) not in visited:
                    region = []
                    touches_border = dfs_helper(i, j, region)

                    if not touches_border:
                        for x, y in region:
                            board[x][y] = 'X'
