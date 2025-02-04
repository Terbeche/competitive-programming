tt = int(input())

for _ in  range(tt):
    n = int(input())
    cards = list(map(int, input().split()))
    answer = 0
    stack = []

    for i in range(n):
        if cards[i] > 0:
            stack.append(cards[i])
        
        elif cards[i] == 0 and stack:
                max_bonus = max(stack)
                answer += max_bonus
                stack.remove(max_bonus)

    print(answer)