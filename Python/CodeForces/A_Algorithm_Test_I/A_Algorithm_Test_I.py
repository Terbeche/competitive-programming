n = int(input())
arr = list(map(int, input().split()))


num = len(set(arr))
answer = 1
for i in range(1, num+1):
    answer = answer * i

print(answer)
