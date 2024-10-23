number = int(input())
answer = 0

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def almost_prime(n):
    count = 0
    for i in range(1, n):
        if is_prime(i) and n % i == 0:
            count += 1
    
    return count == 2

for i in range(1, number+1):
    if almost_prime(i):
        answer += 1

print(answer)