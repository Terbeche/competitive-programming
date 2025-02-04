tt = int(input())


for _ in range(tt):
    n, p1, p2 = list(map(int, input().split()))
    if n % 2 == 0:
        promotion_price = (n // 2) * p2
        regular_price = n * p1
    else:
        promotion_price = (n // 2) * p2 + p1
        regular_price = n * p1
    
    print(min(promotion_price, regular_price))
