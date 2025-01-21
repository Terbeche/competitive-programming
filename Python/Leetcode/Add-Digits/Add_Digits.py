class Solution:
    def addDigits(self, num: int) -> int:

        def addNum(num):
            answer = 0
            while num >= 10:
                answer += num % 10
                num //= 10

            return answer + num
        
        while num >= 10:
            num = addNum(num)

        return num