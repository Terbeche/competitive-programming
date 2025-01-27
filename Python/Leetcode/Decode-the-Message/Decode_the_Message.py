from collections import defaultdict


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        new_key = defaultdict()
        new_key[' '] = ' '

        answer = ""
        j = ord('a')

        for i in range(len(key)):
            if len(new_key) == 27:
                break
            if key[i] not in new_key.keys():
                new_key[key[i]] =  chr(j)
                j += 1

        for i in range(len(message)):
            answer += new_key[message[i]]
        
        return answer