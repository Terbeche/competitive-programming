from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []

        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)):
            number = nums.pop(0)
            permutations = self.permute(nums)

            for permutation in permutations:
                permutation.append(number)
            
            nums.append(number)
            answer.extend(permutations)

        return answer
