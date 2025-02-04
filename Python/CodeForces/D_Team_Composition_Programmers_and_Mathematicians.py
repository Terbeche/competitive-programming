tt = int(input())

def solve():
    for _ in range(tt):
        a, b = list(map(int, input().split()))

        print(min(min(a,b), (a+b)//4))
solve()
