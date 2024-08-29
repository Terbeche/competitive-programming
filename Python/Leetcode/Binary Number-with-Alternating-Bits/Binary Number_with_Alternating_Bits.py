class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        alternative = not (n & 1)
        while(n != 0):
            if n & 1 == alternative:
                return False

            alternative = n & 1

            n = n>>1

        return  True