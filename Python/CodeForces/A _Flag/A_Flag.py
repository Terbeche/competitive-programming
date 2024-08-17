n, m = list(map(int, input().split()))
prev_color = None
flag = True

for i in range(n):
    flag_row = input().strip()
    
    if len(set(flag_row)) != 1:
        flag = False
        break
    
    if prev_color and prev_color == flag_row[0]:
        flag = False
        break
    
    prev_color = flag_row[0]

print("YES" if flag else "NO")
