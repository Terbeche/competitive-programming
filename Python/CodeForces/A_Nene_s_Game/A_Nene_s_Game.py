tt = int(input())

for _ in range(tt):
    k, n = list(map(int, input().split()))
    a = list(map(int, input().split()))
    q = list(map(int, input().split()))

        
    min_a = min(a)
    result = []
    for i in range(len(q)):
        if q[i] < min_a:
            result.append(q[i])
        else:
            result.append(min_a - 1)

    print(*result)
