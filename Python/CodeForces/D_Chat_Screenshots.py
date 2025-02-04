from collections import defaultdict, deque

tt = int(input())
for _ in range(tt):
    n, k = map(int, input().split())
    graph = defaultdict(list)
    parents =  [0] * (n+1)

    for _ in range(k):
        arr = list(map(int, input().split()))
        for i in range(1, len(arr) - 1):
            graph[arr[i]].append(arr[i + 1])
            parents[arr[i+1]] += 1
    
    queue = deque()
    for i in range(1, n + 1):
        if parents[i] == 0:
            queue.append(i)

    answer = []
    while queue:
        node = queue.popleft()
        answer.append(node)
        for child in graph[node]:
            parents[child] -= 1
            if parents[child] == 0:
                queue.append(child)

    print('YES') if len(answer) == n else print('NO')