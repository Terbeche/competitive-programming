tt = int(input())

for _ in range(tt):
    arr = list(map(int, input()))
    if arr == sorted(arr):
        print(1)
    elif arr[::-1] == sorted(arr):
        print(2)
    else:
        count = 0

        for i in range(1, len(arr)):
            if arr[i] != arr[i-1]:
                count += 1
        
        print(count)
