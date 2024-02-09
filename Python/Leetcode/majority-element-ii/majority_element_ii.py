class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        answer = []
        times  = len(nums) / 3

        for num in set(nums):
            if nums.count(num) > times:
                answer.append(num)
        
        return answer
