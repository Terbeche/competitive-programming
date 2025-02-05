n = int(input())

arr  = list(map(int, input().split()))

first_answer = []
second_answer = []


left, right = 0, len(arr)- 1

while left <= right:
    if left == right:
        first_answer.append(arr[left])
        break
    if arr[left] >= arr[right]:
        first_answer.append(arr[left])
        left += 1
    else:
        first_answer.append(arr[right])
        right -=1
    if arr[left] >= arr[right]:
        second_answer.append(arr[left])
        left += 1
    else:
        second_answer.append(arr[right])
        right -=1


print(sum(first_answer), sum(second_answer))
