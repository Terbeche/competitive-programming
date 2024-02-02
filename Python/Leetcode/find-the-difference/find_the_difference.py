class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for char in t:
            if s.count(char) != t.count(char):
                return char
