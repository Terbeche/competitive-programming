import sys

s = sys.stdin.readline().strip()
m = int(sys.stdin.readline().strip())

cumulative_counting = [0] * len(s)

count = 0

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    cumulative_counting[i] = count

answer = []

for _ in range(m):
    left, right = map(int, sys.stdin.readline().split())
    answer.append(str(cumulative_counting[right - 1] - cumulative_counting[left - 1]))

sys.stdout.write('\n'.join(answer))
