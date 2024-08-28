from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        bit = 1

        for i in range(1, n + 1):
            if i == bit * 2:
                bit = i

            dp[i] = 1 + dp[i - bit]

        return dp