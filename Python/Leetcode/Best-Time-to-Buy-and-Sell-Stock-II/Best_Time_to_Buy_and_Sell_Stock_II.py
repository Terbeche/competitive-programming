from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        answer = 0
        i = 1
        while i < n:
            if prices[i-1] < prices[i]:
                start = prices[i-1]
                while i < n and prices[i-1] < prices[i]:
                    i += 1
                end = prices[i-1]

                answer += end -start
            i += 1

        return answer