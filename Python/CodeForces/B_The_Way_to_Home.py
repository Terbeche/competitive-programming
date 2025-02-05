n, d = list(map(int, input().split()))

lilies = input()

point = 0
answer = 0
flag = True
while point < len(lilies)-1:
    point = min(point + d, len(lilies)-1)
    temp_d = d
    while temp_d > 0:
        if lilies[point] != "1":
            point -= 1
            temp_d -= 1
        else:
            answer += 1
            break
    
    if temp_d == 0:
        flag = False
        print("-1")
        break

if flag:
    print(answer)