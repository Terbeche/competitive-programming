class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        answer = ""
        while columnNumber > 0:
            columnNumber -= 1
            answer += chr(ord('A') + int(columnNumber % 26))
            columnNumber //= 26

        return answer[::-1]