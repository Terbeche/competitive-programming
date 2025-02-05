n = int(input())
planets = list(map(int, input().split()))

big_resource = max(planets)
freq = [0] * (big_resource + 1)

for i in planets:
    freq[i] += i

dp = [0] * (big_resource + 1)

dp[0] = 0

dp[1] = freq[1]

for i in range(2, big_resource + 1):
    dp[i] = max(dp[i - 1], dp[i - 2] + freq[i])

print(dp[big_resource])
