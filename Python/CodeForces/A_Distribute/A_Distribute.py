n = int(input())
arr = list(map(int, input().split()))

target = sum(arr) // (n // 2) 
dp = {}

for i in range(0, n):
    for j in range(i+1, n):
        if (j+1 not in dp and i+1 not in dp) and (arr[i] + arr[j] == target):
            dp[i+1] = j+1
            dp[j+1] = i+1

arr_ = []
for key, val in dp.items():
    arr_.append([key, val])

answer = []
for i in range(0, n, 2):
    answer.append(arr_[i])

for ele in answer:
    print(*ele)