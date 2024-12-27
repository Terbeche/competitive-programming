class Solution:
    def hammingWeight(self, n: int) -> int:
        answer = 0
        while n:
            answer += n & 1
            n >>= 1
        return answer
