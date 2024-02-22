class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        result = []
        never_lost = set()
        lost_once = set()

        losses = {}
            
        for match in matches:
            winner, loser = match

            if loser in losses:
                losses[loser] += 1
                if loser in lost_once:
                    lost_once.remove(loser)

            else:
                losses[loser] = 1
                lost_once.add(loser)

            if loser in never_lost:
                never_lost.remove(loser)

            if winner not in losses:
                never_lost.add(winner)

        result.append(sorted(never_lost))
        result.append(sorted(lost_once))
        return result
