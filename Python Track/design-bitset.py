class Bitset:

    def __init__(self, size: int):
        self.arr = ['0'] * size
        self.ones = 0
        self.fliped = True

    def fix(self, idx: int) -> None:
        if(self.fliped):
            if(self.arr[idx] == '0'):
                self.arr[idx] = '1'
                self.ones+=1
        else:
            if(self.arr[idx] == '1'):
                self.arr[idx] = '0'
                self.ones+=1

    def unfix(self, idx: int) -> None:
        if(self.fliped):
            if(self.arr[idx] == '1'):
                self.arr[idx] = '0'
                self.ones-=1
        else:
            if(self.arr[idx] == '0'):
                self.arr[idx] = '1'
                self.ones-=1

    def flip(self) -> None:
        self.ones = len(self.arr) - self.ones 
        if(self.fliped):
            self.fliped = False
        else:
            self.fliped = True


    def all(self) -> bool:
        return len(self.arr) == self.ones 

    def one(self) -> bool:
        return self.ones

    def count(self) -> int:
        return self.ones 

    def toString(self) -> str:
        if(self.fliped):

            return ''.join(self.arr)
        else:
            return ''.join(['1' if i == '0' else '0' for i in self.arr])


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.ones()
# param_7 = obj.toString()