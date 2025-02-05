n, k = list(map(int, input().split()))
 
arr = list(map(int, input().split()))
 
current_sum = sum(arr[:k])
min_sum = current_sum
answer = 1

for i in range(1, n-k+1):
    current_sum = current_sum - arr[i-1] + arr[i+k-1]
    if min_sum > current_sum:
        min_sum = current_sum
        answer = i+1
print(answer)
