n = int(input())
p  = list(map(int, input().split()))

trees = [i for i in range(n+1)] 
answer = set()

def find(bab):
    if trees[bab] != bab:
        trees[bab] = find(trees[bab])
    return trees[bab]


def union(bab1, bab2):
    tree1, tree2 = find(bab1), find(bab2)

    if tree1 != tree2:
        trees[tree2] = tree1


for i in range(n):
    bab1, bab2 = i+1, p[i]
    union(bab1, bab2)

for i in range(1, n+1):
    answer.add(find(i))

print(len(answer))
