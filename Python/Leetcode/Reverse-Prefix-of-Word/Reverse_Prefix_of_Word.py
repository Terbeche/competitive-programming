class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        answer = ""
        n = len(word)

        for i in range(n):
            if word[i] == ch:
                answer += word[0:i+1][::-1]
                break

        if i == n-1 and word[-1] != ch:
            return word
        
        answer += word[i+1:]
        return answer