class Solution:
    def toLowerCase(self, s: str) -> str:
        add = ord('a') - ord('A')
        n = len(s)
        answer = ""
        for i in range(n):
            if ord(s[i]) <= ord('Z') and ord(s[i]) >= ord('A'):
                answer += chr(ord(s[i]) + add) 
            else:
                answer += s[i]
        
        return answer