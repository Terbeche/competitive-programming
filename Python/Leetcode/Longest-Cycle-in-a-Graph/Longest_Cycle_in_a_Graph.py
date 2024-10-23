from typing import List


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        visited = set()
        cycles = []
    
        def dfs(node, current_path):
            if edges[node] == -1:
                return
            
            if edges[node] in current_path:
                cycle_start = edges[node]
                cycle = []
                for x in current_path:
                    if x == cycle_start:
                        cycle.append(x)
                        while x != node:
                            x = edges[x]
                            cycle.append(x)
                        cycles.append(cycle)
                        return
                
            if edges[node] in visited:
                return
                
            current_path.add(node)
            visited.add(node)            
            dfs(edges[node], current_path)
            current_path.remove(node)
    
        for i in range(n):
            if i not in visited:
                dfs(i, set())
                
        answer = -1
        for cycle in cycles:
            answer = max(answer, len(cycle))
        return answer