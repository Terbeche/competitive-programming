class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        result = set()
        not_good = set()

        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                not_good.add(fronts[i])
                continue
            else:
                result.add(fronts[i])
                result.add(backs[i])

        result = { num for num in result if num not in not_good}
        if len(result) > 0:
            return min(result)
        return 0