n, m  = list(map(int, input().split()))

if n < m:
    print(-1)
else:
    answer = n // 2 + n % 2

    if answer % m != 0:
        answer += m - (answer % m)

    if answer > n:
        print(-1)
    else:
        print(answer)
