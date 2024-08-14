from typing import List

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()
        visited = set()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j, 0))
                    visited.add((i, j))

        if len(queue) == 0 or len(queue) == n * n:
            return -1

        answer = -1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            x, y, distance = queue.popleft()
            answer = max(answer, distance)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, distance + 1))

        return answer