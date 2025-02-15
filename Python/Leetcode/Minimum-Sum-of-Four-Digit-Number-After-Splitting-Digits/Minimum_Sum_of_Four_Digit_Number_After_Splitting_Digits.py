class Solution:
    def minimumSum(self, num: int) -> int:
        digits = sorted(map(int, str(num)))

        return (digits[0] + digits[1]) * 10 + (digits[2] + digits[3])
