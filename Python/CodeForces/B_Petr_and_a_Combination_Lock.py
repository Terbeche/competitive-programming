n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

answer = 0

def backtracking(i ,answer):
    if i == len(arr):
        return answer % 360 == 0

    if backtracking(i+1, answer + arr[i]) or   backtracking(i+1, answer - arr[i]):
        return True
    else:
        return False


if backtracking(0, answer):
    print("YES")
else:
    print("NO")