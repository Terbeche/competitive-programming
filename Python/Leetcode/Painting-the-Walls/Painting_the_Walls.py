from typing import List


class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for c, t in zip(cost, time):
            for i in range(n, 0, -1):
                dp[i] = min(dp[i], dp[max(i - t - 1, 0)] + c)
        
        return dp[n]
