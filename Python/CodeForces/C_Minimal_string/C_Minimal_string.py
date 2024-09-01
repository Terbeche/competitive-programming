from collections import Counter

s = input()
dict = Counter(s)
t = []
u = []

for i in s:
    t.append(i)
    dict[i]-=1
    if dict[i]==0:
        del dict[i] 
    while t and (not dict or min(dict) >= t[-1]):
        u.append(t.pop())

print(''.join(u))
