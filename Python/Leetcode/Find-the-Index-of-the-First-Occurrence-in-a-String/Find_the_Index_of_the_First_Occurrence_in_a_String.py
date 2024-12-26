class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        if needle in haystack:
            for i in range(n):
                if haystack[i] == needle[0]:
                    if haystack[i:i+m] == needle:
                        return i
        return -1