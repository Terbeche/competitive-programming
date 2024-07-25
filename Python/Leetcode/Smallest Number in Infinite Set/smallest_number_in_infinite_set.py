from heapq import heappop, heappush


class SmallestInfiniteSet:

    def __init__(self):
        self.min_num = 1
        self.added_nums = set()
        self.min_heap = []

    def popSmallest(self) -> int:
        if self.min_heap:
            smallest = heappop(self.min_heap)
            self.added_nums.remove(smallest)
            return smallest
        else:
            smallest = self.min_num
            self.min_num += 1
            return smallest        

    def addBack(self, num: int) -> None:    
        if num < self.min_num and num not in self.added_nums:
            self.added_nums.add(num)
            heappush(self.min_heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)