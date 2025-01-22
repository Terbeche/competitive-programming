from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code_morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        words_converted = []
        for word in words:
            word_con = ""
            for letter in word:
                word_con += code_morse[ord(letter) - ord("a")]
            
            words_converted.append(word_con)
        
        return len(set(words_converted))