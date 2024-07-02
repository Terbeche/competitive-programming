class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        queue = deque()

        for row in range(m):
            for col in range(n):
                if isWater[row][col] == 1:
                    queue.append((row, col))
                    isWater[row][col] = 0
                else:
                    isWater[row][col] = -1

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < m and 0 <= new_col < n and isWater[new_row][new_col] == -1:
                    isWater[new_row][new_col] = isWater[row][col] + 1
                    queue.append((new_row, new_col))

        return isWater
