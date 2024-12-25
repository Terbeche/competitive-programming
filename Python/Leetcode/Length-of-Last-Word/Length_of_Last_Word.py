class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        answer = 0
        point = len(s) -1 
         
        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                point -= 1
            else:
                break

        for i in range(point, -1, -1):
            if s[i] != " ":
                answer += 1
            else:
                break
        
        return answer