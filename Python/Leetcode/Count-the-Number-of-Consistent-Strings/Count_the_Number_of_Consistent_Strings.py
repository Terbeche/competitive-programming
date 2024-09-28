class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        

        count = 0

        for word in words:
            not_consistent = False
            for letter in word:
                if allowed.count(letter) == 0:
                    not_consistent = True
                    break
            if not_consistent:
                continue
            else:
                count += 1

        return count