class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        answer = ""

        if len(word1) > len(word2):
            short_word = word2
            long_word = word1
            
        else:
            short_word = word1
            long_word = word2

        for i in range(len(short_word)):
            answer += word1[i]
            answer += word2[i]

        answer += long_word[len(short_word):]
        
        return answer