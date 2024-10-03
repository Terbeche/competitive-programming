from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        n = len(prices)

        def dfs(i , buy):
            if i >= n:
                return 0
            
            if (i, buy) in dp:
                return dp[(i, buy)]

            cooldown = dfs(i + 1, buy)
            if buy:
                buying = dfs(i + 1, not buy) - prices[i]                
                dp[(i, buy)] = max(buying, cooldown)
            else:
                selling = dfs(i + 2, not buy) + prices[i]
                dp[(i, buy)] = max(selling, cooldown)
            
            return dp[(i, buy)]

        return dfs(0, True)