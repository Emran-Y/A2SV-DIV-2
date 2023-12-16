class FrequencyTracker:

    def __init__(self):
        self.dict = {}
        self.feq = {}

    def add(self, number: int) -> None:
        if(number in self.dict):
            self.feq[self.dict[number]] = self.feq[self.dict[number]] - 1
            if(self.feq[self.dict[number]] == 0):
                del self.feq[self.dict[number]]
        self.dict[number] = 1 + self.dict.get(number,0)
        self.feq[self.dict[number]] = 1 + self.feq.get(self.dict[number],0)

    def deleteOne(self, number: int) -> None:
        if(number in self.dict):
            self.feq[self.dict[number]] = self.feq[self.dict[number]] - 1
            if(self.feq[self.dict[number]] == 0):
                del self.feq[self.dict[number]]
            self.dict[number] =  self.dict[number] - 1
            

            if(self.dict[number] == 0): 
                del self.dict[number]
            else:
                self.feq[self.dict[number]] = 1 + self.feq.get(self.dict[number],0)

    def hasFrequency(self, frequency: int) -> bool:
        if(frequency in self.feq):
            return True
        else:
            return False


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)