class Solution:
    def minTimeToType(self, word: str) -> int:
        start_diff = abs(ord(word[0]) - ord('a'))
        answer = min(start_diff, 26 - start_diff) + 1
        
        for i in range(len(word)-1):
            diff = abs(ord(word[i]) - ord(word[i+1]))
            answer += min(diff, 26 - diff) + 1

        return answer