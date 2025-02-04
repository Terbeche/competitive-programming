n, s = list(map(int, input().split()))
arr = list(map(int, input().split()))


answer = 0
left, right = 0,0


dict = {}

while right < len(arr):
    if arr[right] not in dict:
        dict[arr[right]] = 0
    
    dict[arr[right]] += 1

    while len(dict) > s:
        dict[arr[left]] -= 1
        if dict[arr[left]] == 0:
            del dict[arr[left]]

        left += 1
    answer += right - left + 1

    right += 1

print(answer) 