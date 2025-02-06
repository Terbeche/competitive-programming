n = int(input())

arr = []
arr.append(n)

for number in range(1, n):
    arr.append(number)
print(*arr)