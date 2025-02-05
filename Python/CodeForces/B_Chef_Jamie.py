n = int(input())
fruits = list(map(int, input().split()))

sorted_fruits = sorted(fruits)
answer = 0

for i in range(n):
    if sorted_fruits[i] != fruits[i]:
        answer += 1

print(answer - 1)
