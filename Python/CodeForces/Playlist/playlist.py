from heapq import heappop, heappush

n, k = list(map(int, input().split()))
songs = []
answer = 0

for i in range(n):
    l, b = list(map(int, input().split()))
    songs.append((l, b))

songs.sort(key=lambda x: x[1], reverse=True)
min_heap = []
totol_len = 0

for l, b in songs:
    totol_len += l
    heappush(min_heap, l)

    if len(min_heap) > k:
        totol_len -= heappop(min_heap)

    answer = max(answer, totol_len *b )

print(answer)