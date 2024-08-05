from collections import defaultdict, deque

n, m = list(map(int, input().split()))
count = 0
graph = defaultdict(list)

for _ in range(m):
    u, v = list(map (int, input().split()))
    graph[u].append(v)
    graph[v].append(u)

visited  = [False] * (n + 1)

for i in range(1, n + 1):
    if not visited[i]:
        queue = deque([i])
        visited[i] = True
        component = []
    
        while queue:
            current = queue.popleft()
            component.append(current) 
            for neighbour in graph[current]:
                if not visited [neighbour]:
                    visited[neighbour] = True
                    queue.append(neighbour)
        
        is_cycle = True
        for node in component:
            if len(graph[node]) != 2:
                is_cycle = False
                break

        if is_cycle:
            count += 1

print(count)
