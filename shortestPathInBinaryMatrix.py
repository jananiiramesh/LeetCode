from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        directions = [(-1,0),(+1,0),(0,-1),(0,+1),(-1,-1),(-1,+1),(+1,-1),(+1,+1)]

        queue = deque([(0,0,1)])
        visited = {(0,0)}

        while queue:
            x, y, dist = queue.popleft()

            if x == n-1 and y == n-1:
                return dist

            for dx, dy in directions:
                if 0 <= x + dx < n and 0 <= y + dy < n and grid[x+dx][y+dy] != 1 and (x+dx, y+dy) not in visited:
                    queue.append((x+dx, y+dy, dist+1))
                    visited.add((x+dx, y+dy))

        return -1

        
