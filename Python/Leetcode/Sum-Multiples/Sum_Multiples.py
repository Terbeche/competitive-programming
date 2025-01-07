class Solution:
    def sumOfMultiples(self, n: int) -> int:
        answer = 0
        for num in range(n+1):
            if num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
                answer += num

        return answer