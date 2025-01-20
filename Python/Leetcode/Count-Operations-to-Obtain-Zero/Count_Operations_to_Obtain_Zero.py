class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        answer = 0

        while num1 != 0 and num2 != 0:
            if num1 >= num2:
                num1 = num1 - num2
            else:
                num2 = num2 - num1

            answer += 1

        return answer
