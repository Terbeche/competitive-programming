class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [float('inf')] * (amount + 1)
        
        def backtracking(remaining):
            if remaining == 0:
                return 0
            if remaining < 0:
                return -1
            
            if memo[remaining] != float('inf'):
                return memo[remaining]
            
            min_coins = float('inf')
            
            for coin in coins:
                result = backtracking(remaining - coin)
                if result >= 0:
                    min_coins = min(min_coins, result + 1)
            
            memo[remaining] = -1 if min_coins == float('inf') else min_coins
            return -1 if min_coins == float('inf') else min_coins
        
        return backtracking(amount)