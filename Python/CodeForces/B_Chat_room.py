s =  list(input())
word = "hello"

i = 0
j = 0


while i < len(s) and j < len(word):
    if s[i] == word[j]:
        i += 1
        j += 1
    else:
        i += 1


if j == len(word):
    print("YES")
else:
    print("NO")