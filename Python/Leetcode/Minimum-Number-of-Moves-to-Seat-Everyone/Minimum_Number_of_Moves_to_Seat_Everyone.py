from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        n = len(seats)
        seats.sort()
        students.sort()
        answer = 0

        for i in range(n):
                answer += abs(seats[i] - students[i])

        return answer