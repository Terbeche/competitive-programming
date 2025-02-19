from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        answer = 0
        for i in range(len(points)- 1):
            x_diff = abs(points[i][0] - points[i+1][0])
            y_diff = abs(points[i][1] - points[i+1][1])
            answer += max(x_diff, y_diff)

        return answer