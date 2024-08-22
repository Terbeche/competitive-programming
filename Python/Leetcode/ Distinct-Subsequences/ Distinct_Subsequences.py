class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        memo = [ [None for _ in range(n+1)] for _ in range(m+1)]

        def backtracking(i, j):
            if memo[j][i] is not None:
                return memo[j][i]
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            
            answer = 0            
            if s[i] == t[j]:
                answer += backtracking(i + 1, j + 1)
            answer += backtracking(i + 1, j)
            
            memo[j][i] = answer
            
            return answer

        return backtracking(0, 0)      
