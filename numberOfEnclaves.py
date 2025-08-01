from collections import deque
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        queue = deque()
        m = len(grid)
        n = len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for i in range(m):
            if grid[i][0] == 1:
                queue.append((i,0))
                grid[i][0] = '#'
            if grid[i][n-1] == 1:
                queue.append((i,n-1))
                grid[i][n-1] = '#'

        for j in range(n):
            if grid[0][j] == 1:
                queue.append((0,j))
                grid[0][j] = '#'
            if grid[m-1][j] == 1:
                queue.append((m-1,j))
                grid[m-1][j] = '#'

        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    queue.append((nx,ny))
                    grid[nx][ny] = '#'

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += 1

        return count
