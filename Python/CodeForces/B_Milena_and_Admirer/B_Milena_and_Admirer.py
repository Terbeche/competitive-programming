tt = int(input())

for _ in range(tt):
    n = int(input())
    arr = list(map(int, input().split()))

    answer = 0
    
    for i in range(n - 2, -1, -1):
        if arr[i] <= arr[i + 1]:
            continue
        
        elements = (arr[i] + arr[i + 1] - 1) // arr[i + 1]
        answer += elements - 1
        
        arr[i] = arr[i] // elements

    print(answer)
