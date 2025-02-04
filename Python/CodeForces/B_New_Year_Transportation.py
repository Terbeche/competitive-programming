n, t = list(map(int, input().split()))

portals = list(map(int, input().split()))

start = 1

for i in range(len(portals)):
    start += portals[start - 1]
    if start == t:
        print("YES")
        break
    elif start > t:
        print("NO")
        break