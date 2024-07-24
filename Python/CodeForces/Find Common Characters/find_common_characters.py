class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        char_counts = {}
    
        for char in words[0]:
            char_counts[char] = char_counts.get(char, 0) + 1
        
        # Update character counts based on the remaining words
        for word in words[1:]:
            temp_counts = {}
            for char in word:
                if char in char_counts:
                    temp_counts[char] = temp_counts.get(char, 0) + 1
                    char_counts[char] -= 1
                    if char_counts[char] == 0:
                        del char_counts[char]
            char_counts = temp_counts
        
        result = []
        for char, count in char_counts.items():
            result.extend([char] * count)
        
        return result
