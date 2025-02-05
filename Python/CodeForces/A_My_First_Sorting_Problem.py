tt = int(input())


for _ in range(tt):
    n, m = list(map(int, input().split()))

    print(min(n,m),max(n,m))
