from collections import defaultdict, deque
import math
from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(bombs)
        answer = 0
    
        for i in range(n):
            x1, y1, radius1 = bombs[i]
            for j in range(n):
                if i != j:
                    x2, y2, radius2 = bombs[j]
                    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                    if distance <= radius1:
                        graph[i].append(j)

        def bfs(start):
            queue = deque([start])
            visited = set([start])
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            return len(visited)
    
        for i in range(len(bombs)):
            answer = max(answer, bfs(i))

        return  answer
