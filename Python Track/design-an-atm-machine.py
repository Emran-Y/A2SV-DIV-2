class ATM:

    def __init__(self):
        self.tot = [0] * 5
        self.denominations = {0: 20, 1: 50, 2: 100, 3: 200, 4: 500}

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.tot[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        temp = self.tot.copy()
        ans = [0] * 5

        for i in range(4, -1, -1):
            if amount >= self.denominations[i] and temp[i] != 0:
                num = min(amount // self.denominations[i], temp[i])
                temp[i] -= num
                amount -= num * self.denominations[i]
                ans[i] = num

        if amount == 0:
            self.tot = temp
            return ans
        else:
            return [-1]