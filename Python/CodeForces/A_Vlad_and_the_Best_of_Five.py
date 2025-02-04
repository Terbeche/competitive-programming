from collections import Counter

tt = int(input())

for _ in range(tt):
    s = input()
    s_counter = Counter(s)

    if s_counter['A'] >  s_counter['B']:
        print('A')
    else:
        print('B')