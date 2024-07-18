n = int(input())
arr = list(map(int, input().split()))
answer = 0

min_positive = float("inf")
positive_counter = 0

for i in range(n):
    if arr[i] > 0 and arr[i] % 2 != 0:
        min_positive = min(min_positive, arr[i])

    if arr[i] > 0:
        positive_counter += 1
        answer += arr[i]

max_negative = float("-inf")
for i in range(n):
    if arr[i] < 0 and arr[i] % 2 != 0:
        max_negative = max(max_negative, arr[i])

if answer % 2 != 0:
    print(answer)
elif positive_counter == n:
    print(answer - min_positive)
else:
    print(max(answer + max_negative,answer - min_positive))
