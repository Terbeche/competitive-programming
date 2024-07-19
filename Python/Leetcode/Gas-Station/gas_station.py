class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_diff = 0
        curr_diff = 0
        start = 0

        for i in range(len(gas)):
            total_diff += gas[i] - cost[i]
            curr_diff += gas[i] - cost[i]

            if curr_diff < 0:
                curr_diff = 0
                start = i + 1

        if total_diff < 0:
            return -1
        else:
            return start
