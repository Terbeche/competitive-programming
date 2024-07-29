n = int(input())
experiments = []

for _ in range(n):
    start, end, rooms = map(int, input().split())
    experiments.append((start, 1, rooms))
    experiments.append((end + 1, -1, rooms))

experiments.sort()

current_rooms = 0
answer = 0

for _, experiment_type, rooms in experiments:
    if experiment_type == 1:
        current_rooms += rooms
    else:
        current_rooms -= rooms
    
    answer = max(answer, current_rooms)

print(answer)