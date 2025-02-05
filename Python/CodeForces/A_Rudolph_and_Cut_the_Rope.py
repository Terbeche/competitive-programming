tt = int(input())

for _ in  range(tt):
    nails = int(input())
    answer = 0
    for i in range(nails):
        
        h, l = list(map(int, input().split()))
        if h > l:
            answer += 1

    print(answer)
