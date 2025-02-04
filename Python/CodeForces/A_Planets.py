from collections import Counter


tt = int(input())

for _ in range(tt):
    n, cost = list(map(int, input().split()))
    planets =  list(map(int, input().split()))
    answer = 0

    planets_count = Counter(planets)

    for key,val in planets_count.items():
        if val == 1:
            answer += 1
        else:
            answer += min(val, cost)

    print(answer)