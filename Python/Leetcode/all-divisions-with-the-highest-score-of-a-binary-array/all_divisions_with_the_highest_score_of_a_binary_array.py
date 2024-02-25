class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        division_score = {}
        result = []
        zeros_count = 0
        ones_count = sum(nums)

        for i in range(len(nums)):
            division_score[i] = zeros_count + ones_count
            division_score[len(nums)] = zeros_count 

            if nums[i] == 0:
                zeros_count += 1
            else:
                ones_count -= 1
        
        if nums[len(nums) - 1] == 0:
            division_score[len(nums)] += 1

        max_division_score = 0
        for key, value in division_score.items():
            max_division_score = max(max_division_score,value)

        for key, value in division_score.items():
            if value == max_division_score:
                result.append(key)
    
        return result
