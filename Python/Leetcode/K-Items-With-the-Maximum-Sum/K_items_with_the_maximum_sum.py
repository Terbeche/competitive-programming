class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        answer = 0

        while k > 0:
            if numOnes == 0 and numZeros == 0:
                numNegOnes -= 1
                answer -= 1
            elif numOnes == 0:
                numZeros -= 1
            else:
                numOnes -= 1
                answer +=1
            k -= 1
        return answer
