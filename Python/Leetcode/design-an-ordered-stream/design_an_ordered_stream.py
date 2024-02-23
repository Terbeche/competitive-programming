class OrderedStream:

    def __init__(self, n: int):
        self.values_number = n
        self.values = [None] * n
        self.current = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.values[idKey - 1] = value
        result = []

        while self.current < self.values_number and self.values[self.current] is not None:
            result.append(self.values[self.current])
            self.current += 1
        
        return result

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
