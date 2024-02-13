class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = list(s.split())
        s_list_length = len(s_list)
        
        result = ""

        for i in range(s_list_length - 1, -1, -1):
            result += s_list[i] + " "

        return result.strip()
