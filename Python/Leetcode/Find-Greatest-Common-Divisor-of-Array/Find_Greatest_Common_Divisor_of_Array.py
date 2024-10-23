from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        num1, num2 = nums[0], nums[-1]

        answer = 0

        for i in range(1, num2+1):
            if num1 % i == 0 and num2 % i == 0:
                answer = i

        return answer