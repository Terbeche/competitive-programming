class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def solve(i, j, k):
            if k == len(num):
                return True
            
            num1, num2 = num[i:j], num[j:k]
            
            if (num1[0] == '0' and len(num1) > 1) or (num2[0] == '0' and len(num2) > 1):
                return False
            
            sum_str = str(int(num1) + int(num2))
            if not num.startswith(sum_str, k):
                return False
 
            return solve(j, k, k + len(sum_str))

        n = len(num)
        for i in range(1, n):
            for j in range(i + 1, n):
                if solve(0, i, j):
                    return True
        return False