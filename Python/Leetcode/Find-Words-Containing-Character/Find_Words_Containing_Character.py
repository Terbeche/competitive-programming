class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        n = len(words)
        answer = []

        for i in range(n):
            if x in words[i]:
                answer.append(i)

        return answer