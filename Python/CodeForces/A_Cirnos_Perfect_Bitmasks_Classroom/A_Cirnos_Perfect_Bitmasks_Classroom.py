def solve(x):
    if x == 1:
        return 3
    
    min_y = x & -x
    
    if x == min_y:
        return min_y + 1

    return min_y

tt = int(input())
for _ in range(tt):
    x = int(input())
    print(solve(x))