from typing import List


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n + 1)]
        for u, v, d in roads:
            graph[u].append((v, d))
            graph[v].append((u, d))
        
        visited = set()
        answer = float('inf')
        
        def dfs(node):
            nonlocal answer
            if node in visited:
                return
            visited.add(node)
            for neighbor, distance in graph[node]:
                answer = min(answer, distance)
                dfs(neighbor)
        
        dfs(1)
        
        return answer