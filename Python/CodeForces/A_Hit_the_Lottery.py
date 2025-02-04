cash = int(input())

bills = [100, 20, 10, 5, 1]
answer = 0

while cash > 0:
    for bill in bills:
        if cash % bill == 0:
            answer +=  cash // bill
            cash = 0
            break

        if cash >= bill:
            cash -= bill
            answer += 1
            break


print(answer)