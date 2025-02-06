n = int(input())
cubes = list(map(int, input().split()))

cubes.sort()
print(*cubes)