from collections import defaultdict, deque
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for i in range(len(equations)):
            graph[equations[i][0]].append((equations[i][1], values[i]))
            graph[equations[i][1]].append((equations[i][0], 1 / values[i]))

        def bfs(numerator, denominator):
            if numerator not in graph or denominator not in graph:
                return -1

            queue = deque()
            visited = set()

            queue.append((numerator, 1))
            visited.add(numerator)

            while queue:
                node, val = queue.popleft()
                if node == denominator:
                    return val
                for nei, weight in graph[node]:
                    if nei not in visited:
                        queue.append((nei, val * weight))
                        visited.add(nei)
            return -1

        answer = []
        for q in queries:
            answer.append(bfs(q[0], q[1]))

        return answer