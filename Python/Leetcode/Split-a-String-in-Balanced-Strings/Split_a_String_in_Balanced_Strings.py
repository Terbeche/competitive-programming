class Solution:
    def balancedStringSplit(self, s: str) -> int:
        n = len(s)
        answer = 0
        count_r = 0
        count_l = 0

        for i in range(n):
            if s[i] == 'R':
                count_r += 1 
            else:
                count_l += 1
            
            if count_l > 0 and count_l == count_r:
                answer += 1
                count_l = 0
                count_r = 0

        return answer