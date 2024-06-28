from collections import defaultdict, deque
from typing import List


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red_edges_graph = defaultdict(list)
        blue_edges_graph = defaultdict(list)

        for start, destination in redEdges:
            red_edges_graph[start].append(destination)
        
        for start, destination in blueEdges:
            blue_edges_graph[start].append(destination)

        queue = deque()
        answer = [ -1 for i in range(n)]

        queue.append([0, 0, None])
        
        visited = set()
        visited.add((0, None))

        while queue:
            curr, length, edge_color = queue.popleft()
            if answer[curr] == -1:
                answer[curr] = length

            if edge_color != "RED":
                for node in red_edges_graph[curr]:
                    if (node, "RED") not in visited:
                        visited.add((node, "RED"))
                        queue.append([node, length + 1, "RED"])

            
            if edge_color != "BLUE":
                for node in blue_edges_graph[curr]:
                    if (node, "BLUE") not in visited:
                        visited.add((node, "BLUE"))
                        queue.append([node, length + 1, "BLUE"])

        return answer
