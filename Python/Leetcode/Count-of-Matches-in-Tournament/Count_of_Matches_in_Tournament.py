class Solution:
    def numberOfMatches(self, n: int) -> int:
        answer = 0
        while n > 1:
            if n % 2 == 0:
                n //= 2
                answer += n
            else:
                n = (n + 1) // 2
                answer += n - 1
        
        return answer