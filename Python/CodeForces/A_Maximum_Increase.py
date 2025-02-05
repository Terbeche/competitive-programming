n = int(input())
arr = list(map(int, input().split()))

answer = 0
current_max = 1

for i in range(1, n):
    if arr[i] > arr[i-1]:
        current_max += 1
    else:
        answer = max(answer, current_max)
        current_max = 1

answer = max(answer, current_max)
print(answer)