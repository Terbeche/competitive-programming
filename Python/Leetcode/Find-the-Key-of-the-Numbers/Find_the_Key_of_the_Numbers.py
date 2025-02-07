from math import floor


class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        nums = [num1, num2, num3]
        answer = 0
        for i in range(4):
            min_ = 9
            for j in range(len(nums)):
                min_ =  min(nums[j] % 10, min_)
                nums[j] = floor(nums[j] / 10)

            answer += min_ * pow(10,i)
        return answer
