tt = int(input())

for _ in range(tt):
    n, m, k = list(map(int, input().split()))
    
    dp = [[set() for _ in range(m + 1)] for _ in range(n + 1)]
    dp[1][1] = {0}
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
                
            if j > 1:
                for cost in dp[i][j-1]:
                    dp[i][j].add(cost + i)

            if i > 1:
                for cost in dp[i-1][j]:
                    dp[i][j].add(cost + j)

    if (k in dp[n][m]):
        print("YES")
    else:
        print("NO")