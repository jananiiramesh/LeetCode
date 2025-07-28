from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        m = len(image)
        n = len(image[0])

        neighbours = [(-1,0),(1,0),(0,-1),(0,1)]
        base_color = image[sr][sc]
        if base_color == color:
            return image
            
        image[sr][sc] = color
        queue = deque([(sr,sc)])
        while queue:
            length = len(queue)
            for _ in range(length):
                node_x, node_y = queue.popleft()
                for nx, ny in neighbours:
                    if 0 <= node_x - nx < m and 0 <= node_y - ny < n and image[node_x - nx][node_y - ny] == base_color:
                        image[node_x - nx][node_y - ny] = color
                        queue.append((node_x - nx, node_y - ny))

        return image
