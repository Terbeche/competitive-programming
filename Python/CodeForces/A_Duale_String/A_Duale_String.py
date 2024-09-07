tt = int(input())

for _ in range(tt):
    s = input()
    n = len(s)

    if (s[0:n//2] == s[n//2:]):
        print("YES")
    else:
        print("NO")
