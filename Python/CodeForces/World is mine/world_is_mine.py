import heapq

tt = int(input())

for _ in range(tt):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    count = [0] * (arr[-1] + 1)
    distinct = [0] * (arr[-1] + 1) 
    
    for x in arr:
        count[x] += 1

    for i in range(1, len(distinct)):
        distinct[i] = distinct[i-1]+ bool (count[i])
    
    heap = []
    taken = 0
    weight = 0

    for x in sorted(set(arr)):
        weight += count[x]
        heapq.heappush (heap, -count [x])
        taken += 1
        while weight > distinct [x] - taken:
            weight += heapq.heappop(heap)
            taken -= 1
    
    print(distinct[-1] - taken)
