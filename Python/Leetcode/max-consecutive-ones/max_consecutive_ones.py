class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        answer = 0
        current_answer = 0
        for num in nums:
            if num == 1:
                current_answer += 1
            else:
                current_answer = 0
                continue
            if current_answer > answer:
                answer = current_answer
    
        return answer
