from collections import deque

n = int(input())
edges = [list(map(int, input().split())) for _ in range(n - 1)]
sequence = list(map(int, input().split()))

def is_valid_bfs(n, edges, sequence):
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    if sequence[0] != 1:
        return False
    
    visited = [False] * (n + 1)
    visited[1] = True
    queue = deque([1])
    seq_index = 1
    
    while queue:
        node = queue.popleft()
        
        neighbors = [neighbor for neighbor in graph[node] if not visited[neighbor]]
        
        neighbor_set = set(neighbors)
        while seq_index < n and sequence[seq_index] in neighbor_set:
            neighbor = sequence[seq_index]
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                neighbor_set.remove(neighbor)
            seq_index += 1
        
        if neighbor_set:
            return False
    
    return all(visited[1:])

if is_valid_bfs(n, edges, sequence):
    print("Yes")
else:
    print("No")