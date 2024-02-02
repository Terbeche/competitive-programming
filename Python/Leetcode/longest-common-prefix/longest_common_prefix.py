class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = len(min(strs, key=len))
        common_prefix = ""

        for i in range(length):
            current_letter = ""
            for word in strs:
                current_letter += word[i]
            
            if len(set(current_letter)) == 1:
                common_prefix += word[i]
            else:
                break
        
        return common_prefix
