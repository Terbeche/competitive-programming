tt = int(input())

for _ in range(tt):
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()
    total_sum = [1]
    initial_sum = 0

    for i in range(n):
        initial_sum += arr[i]
        total_sum.append(initial_sum)
    
    def solve(arr,total_sum):
        for i in range(n):
            if arr[i] > total_sum[i]:
                return False
    
        return True

    
    if solve(arr,total_sum):
        print("YES")
    else:
        print("NO")
