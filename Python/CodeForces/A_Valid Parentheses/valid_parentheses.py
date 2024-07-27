s = input()

stack = []
answer = 0

for char in s:
    if char == "(":
        stack.append(char)
    else:
        if stack:
            stack.pop()
            answer += 2
        
print(answer)