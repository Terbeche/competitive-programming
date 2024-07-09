from heapq import heapify, heappop, heappush
from math import floor
from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-val for val in piles]
        heapify(piles)

        for _ in range(k):
            node = -1 * heappop(piles)
            node = node - (floor(node / 2))
            heappush(piles, -1 * node)

        return -1 * sum(piles)
