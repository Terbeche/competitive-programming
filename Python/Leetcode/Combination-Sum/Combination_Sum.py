from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def backtracking(start, current_sum, current_combination):
            if current_sum == target:
                answer.append(current_combination[:])
                return

            if current_sum > target:
                return

            for i in range(start, len(candidates)):
                current_combination.append(candidates[i])
                backtracking(i, current_sum + candidates[i], current_combination)
                current_combination.pop()

        backtracking(0, 0, [])
        return answer