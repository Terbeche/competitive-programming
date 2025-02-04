n  = int(input())

our_string = input()

left, right = 0, 1
answer = 0

if n == 1:
    print(1)
else:
    while right < n  and left < n:
        current_length = 1
        while right < n  and left < n and our_string[left] < our_string[right] and (ord( our_string[right]) - ord( our_string[left]) == 1):
            right += 1
            left += 1
            current_length += 1
        answer = max(answer, current_length)
        left += 1
        right += 1
    print(answer)