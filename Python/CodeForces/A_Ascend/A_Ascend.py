n = int(input())
arr = list(map(int, input().split()))
answer = 1
count = 1
i = 0

while i < n-1:
    if arr[i] < arr[i+1]:
        count += 1
        answer = max(answer, count)
    else:
        count = 1
    i += 1

print(answer)
