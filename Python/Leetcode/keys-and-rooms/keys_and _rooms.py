class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        queue = [0]
        visited = [False] * n

        while queue:
            curr = queue.pop(0)
            visited[curr] = True
            for room in rooms[curr]:
                if not visited[room]:
                    queue.append(room)

        return all(visited)
