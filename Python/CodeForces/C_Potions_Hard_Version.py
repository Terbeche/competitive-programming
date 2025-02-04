from heapq import heappop, heappush


n = int(input())
portions = list(map(int, input().split()))

min_heap = []
health = 0
answer = 0

for portion in portions:
    health += portion
    answer += 1

    if portion < 0:
        heappush(min_heap, portion)

    if health < 0:
        health -= heappop(min_heap)
        answer -= 1

print(answer)