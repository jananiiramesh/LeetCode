from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        queue = deque()
        time = 0
        fresh = 0
        rows = len(grid)
        cols = len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1

        rots = [(-1,0),(1,0),(0,-1),(0,1)]
        while queue and fresh > 0:
            for _ in range(len(queue)):
                x, y = queue.popleft()

                for rx, ry in rots:
                    nx, ny = x + rx, y + ry
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        queue.append((nx,ny))
            
            time += 1

        return time if fresh == 0 else -1
