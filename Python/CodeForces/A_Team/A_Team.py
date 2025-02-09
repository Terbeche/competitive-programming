n = int(input())
answer = 0

for i in range(n):
    solve = list(map(int, input().split()))
    if sum(solve) > 1:
        answer += 1

print(answer)