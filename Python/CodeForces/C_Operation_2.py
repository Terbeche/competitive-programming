a,b = list(map(int, input().split()))

def min_operations(a, b):
    if a == b:
        return 0
    elif a > b:
        return a - b
    elif a < b:
        if b % 2 == 0:
            return 1 + min_operations(a, b // 2)
        else:
            return 2 + min_operations(a, (b + 1) // 2)

print(min_operations(a, b))

