class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.answer = [''] * n
        self.pointer = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.answer[idKey - 1] = value
        temp = []
        while ( self.pointer < len(self.answer) ):
            if(self.answer[self.pointer]):
                temp.append(self.answer[self.pointer])
                self.pointer+=1
            else:
                return temp
        return temp
                    
                
    

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)