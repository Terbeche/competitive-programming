tt = int(input())

for _ in range(tt):
    s = list(input())

    if len(set(s)) == 1:
        print("NO")

    else:
        for i in range(len(s)):
            if s[i] != s[i-1]:
                s[i], s[i-1] = s[i-1], s[i]
                break
    
        print("YES")
        print("".join(s))