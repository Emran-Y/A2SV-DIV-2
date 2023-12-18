class UndergroundSystem:

    def __init__(self):
        self.inTracker = {}
        self.avg  = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.inTracker[id] = (stationName,t) 

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        for key,value in self.inTracker.items():
            if(id == key):
                if value[0] + ' ' + stationName in self.avg:
                    self.avg[value[0] + ' ' + stationName ].append(t - value[1])
                else:
                    self.avg[value[0] + ' ' + stationName ] = [t - value[1]]
                del key

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        for key,value in self.avg.items():
            if key == startStation + ' ' +  endStation:
                return sum(value) / len(value)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)