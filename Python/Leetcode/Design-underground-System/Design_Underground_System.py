class UndergroundSystem:
    def __init__(self):
        self.check_ins = {}  # To store check-in data
        self.travel_times = {}  # To store total travel times and counts

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.check_ins.pop(id)
        travel_time = t - start_time
        if (start_station, stationName) not in self.travel_times:
            self.travel_times[(start_station, stationName)] = [0, 0]  # [total_time, count]
        self.travel_times[(start_station, stationName)][0] += travel_time
        self.travel_times[(start_station, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, count = self.travel_times[(startStation, endStation)]
        return total_time / count

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)