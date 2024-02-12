class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        result = []
        keyboard_rows = [ "qwertyuiop", "asdfghjkl", "zxcvbnm"]

        for word in words:
            if any(all(letter.lower() in row for letter in word) for row in keyboard_rows):
                result.append(word)

        return result