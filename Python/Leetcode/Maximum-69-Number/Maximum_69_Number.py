class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        answer = ""
        for i in range(len(num)):
            if num[i] == "6":
                answer += "9"
                break
            answer += "9"
        
        answer += num[len(answer)::]
        return int(answer)