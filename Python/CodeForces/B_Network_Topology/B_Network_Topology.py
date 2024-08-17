n, m = list(map(int, input().split()))

edges = []
for i in range(m):
    edges.append(list(map(int, input().split())))

node_dict = {i: 0 for i in range(1, n+1)}
for edge in edges:
    node_dict[edge[0]] += 1
    node_dict[edge[1]] += 1

ones = sum(1 for i in node_dict.values() if i == 1)
twos = sum(1 for i in node_dict.values() if i == 2)
nodes_minus_ones = sum(1 for i in node_dict.values() if i == n-1)

if ones == 2 and twos == n-2:
    print("bus topology")
elif twos == n:
    print("ring topology")
elif nodes_minus_ones == 1 and ones == n-1:
    print("star topology")
else:
    print("unknown topology")
