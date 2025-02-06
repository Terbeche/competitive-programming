n, x = list(map(int, input().split()))
arr = list(map(int, input().split()))

prefix_sum = 0
bounces = 1

for i in range(n):
    prefix_sum += arr[i]
    if prefix_sum <= x:
        bounces += 1
    else:
        break

print(bounces)
