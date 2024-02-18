class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        capacity_copy = capacity

        for i in range(len(plants)):
            while plants[i] > capacity_copy:
                steps += 2 * (i)
                capacity_copy = capacity

            capacity_copy -= plants[i]
            steps += 1

        return steps
