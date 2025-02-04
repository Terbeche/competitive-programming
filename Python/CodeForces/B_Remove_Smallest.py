tt = int(input())

for _ in  range(tt):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    flag = True

    for i in range(n-1):
        if abs(arr[i] - arr[i+1]) > 1:
            flag = False
            break 

    if flag:
        print("YES")
    else:
        print("NO")
