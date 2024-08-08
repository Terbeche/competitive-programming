class Solution:
    def tribonacci(self, n: int, memo = {}) -> int:
        if n < 2:
            return n
        if n == 2:
            return 1

        if n not in memo:
            memo[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)

        return memo[n]
