from collections import defaultdict


reposts = int(input())

answer = 2
names_dict = defaultdict()
names_dict["Polycarp".lower()] = 1

total_names = []
for i in range(reposts):
    names = list(input().split())
    total_names.append(names)

for names in total_names:
    names_dict[names[0].lower()] = names_dict[names[2].lower()] + 1

print(max(names_dict.values()))